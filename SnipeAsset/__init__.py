# -*- coding: utf-8 -*-
from SnipeAsset.FlukeDMS import flukeTest
from SnipeAsset.FlukeCSV import FlukeCSV
from SnipeAsset.Update import createAsset, getDetailsByTag, getDetailsByTagOLD, pullAssetLarge, pullLocations, pullModel, updateAsset_PandD, updateAssetModdel,Update
import json
import datetime
import re
import csv
import html
from SnipeAsset.debuger import debug

#{"id":7816,"name":"3443","asset_tag":"3443","serial":"","model":{"id":203,

outattheend = 1
unknown_TestTypes = []
file_LOC = ""
skip = 31
dupes = []
unhandled = []
counterApplianceNumber = 0
duplicates = 0
fialed_appl = 0
passed_appl = 0
learned = {'13a 4way': 1282, 'flash unit': 1129, 'New Appliance': 0}
faild_ID = []
emptycount = 0
ignore_Types = ['lblClientInformation', 'lblClientName', 'lblClientStreet', 'txtClientName', 'txtClientStreet', 'lblClientCityZipCode', 'lblClientCountry', 'txtClientCityZipCode', 'txtClientCountry', 'lblTestInformation', 'lblCOntractor', 'txtContractor', 'txtContractorAddress', 'txtReportTitle', 'lblOnDate', 'txtDate', 'lblSummary', 'lblTotalAppliances', 'lblPassedAppliances', 'lblFailedAppliances', '', 'txtApplianceName', 'txtApplianceDate', 'txtApplianceInterval', 'txtApplianceCode', 'txtApplianceResult', 'txtTestStepName', 'txtTestStepLimit', 'txtTestStepMeasurement', 'txtTestStepResult']
learn = {}

class SnipeITAsset:
    def __init__(self, url, Key):
        self.snipeITUrl = url #snipe IT url, this will be used to create or update assets in snipeIT, this is passed in when the class is initialized and stored as an instance variable for later use when making API calls to snipeIT
        self.apiKey = Key #snipe IT API key, this will be used to authenticate API calls to snipeIT, this is passed in when the class is initialized and stored as an instance variable for later use when making API calls to snipeIT
        self.divlist = [] #this will be used to store all the tests that are found during the processing of the data, this is a list of dictionaries where each dictionary contains all the details for a single test, this will be used later to create or update assets in snipeIT with the correct details for each test and to handle any duplicates or unknown types that are found during the processing of the data
        self.csvList = []
        self.flukeList = []
        self.csv = FlukeCSV() #initialize the fluke csv class
        self.fluke = flukeTest() #initialize the fluke test class
        self.typeSadList = []

    def getDatafromSnipe(self):
        self.data = pullModel(self.snipeITUrl, self.apiKey)
        self.DiviceTypes = {}
        self.outtableName = {}
        self.data = json.loads(self.data)
        for i in self.data["rows"]:
            id = i['id']
            name = i['name']
            number = i['model_number']
            try:
                catNo = i['category']['id']
            except KeyError:
                catNo = 2
            name = html.unescape(name)
            if(number == None):
                number = id
            self.DiviceTypes[number] = {'id': id, 'name': name, 'catNo': catNo}
            self.outtableName[name] = {'id': id, 'number': number, 'catNo': catNo}
        
        self.data = pullLocations(self.snipeITUrl, self.apiKey)
        self.Locations = {}
        self.data = json.loads(self.data)

        for i in self.data["rows"]:
            id = i['id']
            name = i['name']
            name = html.unescape(name)
            self.Locations[name] = id

        self.data = pullAssetLarge(self.snipeITUrl, self.apiKey)
        self.data = json.loads(self.data)
        self.assets = {}
        debug("Debug",len(self.data["rows"]))
        debug("Debug",self.data["total"])
        debug("Debug",self.data)
        for i in self.data["rows"]:
            id = i['id']
            tag = i['asset_tag']
            if(i['next_audit_date'] == None):
                i['next_audit_date'] = {"date": "None"}
            if(i['last_audit_date'] == None):
                i['last_audit_date'] = {"date": "None"}
            if("date" in i['next_audit_date']):
                nextaudit = i['next_audit_date']["date"]
            else:
                nextaudit = None
            
            if("date" in i['last_audit_date']):
                lastaudit = i['last_audit_date']["date"]
            else:
                lastaudit = None
            if("custom_fields" in i):
                if("PatTest_Result" in i["custom_fields"]):
                    result = i["custom_fields"]["PatTest_Result"]
                else:
                    result = "unknown"
            else:
                result = "unknown"
            try:
                model = i['model']['id']
            except KeyError:
                model = 0
            #tag = html.unescape(tag)
            self.assets[tag] = {'id': id, 'model': model, 'next_audit_date': nextaudit, 'last_audit_date': lastaudit}

    
    def getlistofFiles(self, path):
        import os
        for r, d, f in os.walk(path):
            for file in f:
                if '.csv' in file:
                    self.csvList.append(os.path.join(r, file))
                if '.FLK' in file:
                    self.flukeList.append(os.path.join(r, file))

    
    def processFiles(self,file_LOC):
        self.getlistofFiles(file_LOC)
        if(len(self.flukeList) == 0 and len(self.csvList) == 0):
            debug("info","No files found in the specified location.")
            return
        elif(len(self.flukeList) == 0):
            debug("info","No Fluke files found, processing CSV files only...")
            for c in self.csvList:
                debug("info",f"Processing CSV file: {c}")
                self.importfromFlukeCSV(c)
        elif(len(self.csvList) == 0):
            debug("info","No CSV files found, processing Fluke files only...")
            for f in self.flukeList:
                debug("info",f"Processing Fluke file: {f}")
                self.importfromFluke(f)
        else:
            debug("info",f"Found {len(self.flukeList)} Fluke files and {len(self.csvList)} CSV files, processing all files...")
            for f in self.flukeList:
                self.importfromFluke(f)
            for c in self.csvList:
                self.importfromFlukeCSV(c)
    def importfromFluke(self, infile):
        self.divlist += self.fluke.parse(infile) #parse the data from the fluke test file, this will return a list of tests with their results and details. Each test will be a dictionary with the following structure: {'testnum': '1', 'date': '26-Apr-2026', 'appno': '3443', 'testmode': 'PAT', 'site': 'Site 1', 'site1': 'Location 1', 'site2': 'Location 2', 'user': 'User 1', 'des1': '13A EXTENSION', 'loc': 'Location 1', 'visual': 'P', 'tests': {'Earth Continuity': {'limit': '0.1 ohm', 'measurement': '0.05 ohm', 'result': 'P'}, 'Insulation Resistance': {'limit': '> 1 M ohm', 'measurement': '> 1 M ohm', 'result': 'P'}, ...}}
    def importfromFlukeCSV(self, infile):
        self.divlist += self.csv.getfromFlukeSoftwere(infile) #parse the data from the fluke test file, this will return a list of tests with their results and details. Each test will be a dictionary with the following structure: {'testnum': '1', 'date': '26-Apr-2026', 'appno': '3443', 'testmode': 'PAT', 'site': '


    def fixdata(self):
        divlistOut = []
        for divice in self.divlist:
            divice['TypeSnipeID'] = 1 #default type is set to 1, this is the ID for the "Unknown" type in snipeIT, if we are able to find a matching type for this appliance we will update this field with the correct type ID, but if we are not able to find a matching type we will leave it as 1 which will allow us to easily identify and update these appliances later when we have more information about them. This also prevents us from creating duplicate types in snipeIT for each unknown type we encounter, which would make it harder to manage and analyze the data in snipeIT.
            #divice['Type_ID'] = 1 #same as TypeSnipeID, this is used to store the type ID for the appliance, this is the ID that is used to link the appliance to the correct type in snipeIT, if we are not able to find a matching type for this appliance we will leave it as 1 which will allow us to easily identify and update these appliances later when we have more information about them.
            #Check for des1 in the data
            #setting the itemtype field to the value of des1 from the fluke test data, this is the field that we will use to try to match the appliance to a type in snipeIT, if we are able to find a matching type in snipeIT for this value we will update the TypeSnipeID and Type_ID fields with the correct type ID from snipeIT, if we are not able to find a matching type in snipeIT for this value we will leave the TypeSnipeID and Type_ID fields as 1 which is the ID for the "Unknown" type in snipeIT, this will allow us to easily identify and update these appliances later when we have more information about them.
            try:
                divice['date']  =  (datetime.datetime.strptime(divice['date'], "%d-%b-%y")).strftime("%Y-%m-%d")
            except Exception as e:
                debug("error", f"Error processing date for appliance {id}: {e}")
            divice['nextdate'] = str(int(divice['date'].split('-')[0]) + 1) + "-" + divice['date'].split('-')[1] + "-" + str(int(divice['date'].split('-')[2]))
            if("Type_ID" in divice):
                debug("info", "Type found in test data, using value: " + str(divice['Type_ID']))

                if(str(divice['Type_ID']) in self.DiviceTypes):
                    debug("info", "Type found in DiviceTypes, using value: " + str(self.DiviceTypes[str(divice['Type_ID'])]["name"]))
                    divice['TypeSnipeName'] = self.DiviceTypes[str(divice['Type_ID'])]["name"]
                    divice['TypeSnipeID'] = self.DiviceTypes[str(divice['Type_ID'])]["id"]
                else:
                    debug("Error", "Type_ID found in test data but not in DiviceTypes for appliance with ID: " + str(divice.get("id", "unknown")) + ", setting to None Data: "+str(divice))
                    debug("info", "Type not found in DiviceTypes, setting to None")
                    if(str(divice['Type_ID']) not in self.typeSadList):
                        self.typeSadList.append(str(divice['Type_ID']))
                    divice['TypeSnipeName'] = "None"
                    divice['TypeSnipeID'] = 1
            else:
                debug("Error", "Type_ID not found in test data for appliance with ID: " + str(divice.get("id", "unknown")) + ", setting to None Data: "+str(divice))
                debug("info", "Type not found in test data, setting to None")
                divice['TypeSnipeName'] = "None"
                divice['TypeSnipeID'] = 1

                
            #Location prossing:
            if(divice['location'] in self.Locations):
                divice["LocationSnipeID"] = self.Locations[divice['location']]
            else:
                divice["LocationSnipeID"] = 1

            if(divice["id"] in self.assets):
                divice["snipeID"] = self.assets[divice["id"]]["id"]
            else:
                divice["snipeID"] = 0
            divlistOut.append(divice)
        self.divlist = divlistOut
        debug("info", f"_______________________________________________________________________________________________")
        debug("info", f"Finished fixing data, total appliances: {len(self.divlist)}")
        debug("info", f"Types that were found in test data but not in DiviceTypes: {self.typeSadList}")
        debug("info", f"_______________________________________________________________________________________________")


    def snipeITData(self):
        self.sendtoSnipe()
        self.maintenanceCreate()
        debug("info", "Total Appliances Processed: " + str(len(self.divlist)))

    def sendtoSnipe(self): #this function will loop through the list of appliances and send the data to snipeIT to create or update the assets in snipeIT with the correct details for each appliance, this function will also handle any duplicates or unknown types that are found during the processing of the data, if an appliance is found to be a duplicate (i.e. it has the same ID as an existing asset in snipeIT) it will check if the model matches the model in snipeIT for that asset, if it does not match it will update the model in snipeIT with the correct model for that appliance, if it does match it will skip that appliance and move on to the next one, if an appliance is found to have an unknown type (i.e. it has an TypeSnipeID of 1 which is the ID for the "Unknown" type in snipeIT) it will leave it as is which will allow us to easily identify and update these appliances later when we have more information about them.
        for i in self.divlist:
            debug("info", f"Processing appliance {i['id']} for SnipeIT...")
            if(i['id'] == 0):
                return 0
            elif(i['id'] in self.assets):
                debug("info", f"Appliance {i['id']} already exists in main list, checkin info...")
                if(i["TypeSnipeID"] != self.assets[i['id']]["model"]):
                    debug("info", f"Model mismatch for appliance {i['id']}, updating model in SnipeIT...")
                    data = json.loads(updateAssetModdel(self.snipeITUrl,self.apiKey, i["snipeID"], i["TypeSnipeID"], i['id']))
                    if(data["status"] == "error"):
                        debug("error", f"Error updating model for appliance {i['id']} in SnipeIT: {data['messages']} moddel ID: {i['snipeID']} Type ID: {i['TypeSnipeID']}")
                # Impliment update Pass / Fail and maintance date
                else:
                    debug("info", f"Model match for appliance {i['id']}, no update needed...")
            else:
                debug("info", f"Appliance {i['id']} not found in main list, processing for SnipeIT...")
                data = json.loads(createAsset(self.snipeITUrl, self.apiKey, i, i['id']))
                if(data["status"] == "error"):
                    debug("error", f"Error creating appliance {i['id']} in SnipeIT: {data['messages']} moddel ID: {i['snipeID']} Type ID: {i['TypeSnipeID']}")
                else:
                    self.assets[i['id']] = {'id': data["payload"]["id"], 'model': i['TypeSnipeID'], 'next_audit_date': i['nextdate'], 'last_audit_date': i['date']}
    def maintenanceCreate(self):
        debug("info", f"Creating maintenance for appliances...")
        #CreateMatinance(self.divlist,self.snipeITUrl,self.apiKey)
        for i in self.divlist:
            debug("info", f"-----------\nWorking on {i['id']}: ")
            outData = ""
            divice = i
            if(i["id"] in self.assets):
                if(self.assets[i["id"]]["last_audit_date"] == "None" or self.assets[i["id"]]["last_audit_date"] == None):
                    debug("info", f"Appliance {i['id']} has no last audit date in SnipeIT, updating last audit date in SnipeIT...")
                    updateAsset_PandD(self.snipeITUrl,self.apiKey, i["snipeID"], divice["OverallResult"], divice["nextdate"], divice['date'])
                elif(divice["date"] > self.assets[i["id"]]["last_audit_date"]):
                    debug("info", f"Appliance {i['id']} has a next audit date that is later than the one in SnipeIT, updating next audit date in SnipeIT...")
                    updateAsset_PandD(self.snipeITUrl,self.apiKey, i["snipeID"], divice["OverallResult"], divice["nextdate"], divice['date'])

            if(divice["OverallResult"] == "Not In Use"):
                debug("info", f"Asset {i['id']} is not in use, skipping...")
                continue
            outData += json.dumps(divice["Result"], indent=4, separators=(',', ':'))
            debug("info", f"Updating Snipe-IT ID: {i['id']} and date: {divice['date']} with the following data:\n{outData}")
            
            Update(i["id"], i["snipeID"], outData, divice["date"],self.snipeITUrl,self.apiKey)
    
    def exporttoCSV(self, outfile="Output.csv"):

        #Asset Tag,Model Name,Next Audit Date,PatTest_Result,Location
        output = "Asset Tag,Item Name,Model Name,Next Audit Date,PatTest_Result,Location\n"
        for a in self.divlist:
            if(a == 0):
                continue
            debug("info", f"Processing appliance {a['id']} for export...")
            output += f"{a['id']},{a['name']},{a['itemtype']},{a['nextdate']},{a['OverallResult']},{a['location']}\n"

        with open(outfile, "w") as f:
            f.write(output)

    # Import CSV to SnipeIT