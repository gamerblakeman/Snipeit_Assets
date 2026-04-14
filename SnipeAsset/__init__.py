# -*- coding: utf-8 -*-
from SnipeAsset.FlukeDMS import flukeTest
from SnipeAsset.Update import createAsset, getDetailsByTag, getDetailsByTagOLD, pullAssetLarge, pullLocations, pullModel, updateAssetModdel
import json
import datetime
import re
import csv
import html

#{"id":7816,"name":"3443","asset_tag":"3443","serial":"","model":{"id":203,
debuglevel = 0
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
        self.data = pullModel(url, Key)
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
        
        self.data = pullLocations(url, Key)
        self.Locations = {}
        self.data = json.loads(self.data)

        for i in self.data["rows"]:
            id = i['id']
            name = i['name']
            name = html.unescape(name)
            self.Locations[name] = id

        self.data = pullAssetLarge(url, Key)
        self.data = json.loads(self.data)
        self.assets = {}
        print(len(self.data["rows"]))
        print(self.data["total"])
        for i in self.data["rows"]:
            id = i['id']
            tag = i['asset_tag']
            try:
                model = i['model']['id']
            except KeyError:
                model = 0
            #tag = html.unescape(tag)
            self.assets[tag] = {'id': id, 'model': model}
        
        self.snipeITUrl = url
        self.apiKey = Key
        self.dupesdiviceList ={}
        self.Appliances = {}
        self.testtypes = []
        self.ListTypes = {}
        self.unknown_TestTypes = []
        self.csv = []
        self.fluke = []
        self.duplicates = 0
        self.dupes = []
        self.emptycount = 0
        self.lastdisc = 0
        #self.DiviceTypes = {1156:"13A > 15A ADAPTER",1157:"15A > 13A ADAPTER",1158:"13A > 16A ADAPTER",1159:"16A > 13A ADAPTER",1160:"16A > 15A ADAPTER",1161:"15A > 16A ADAPTER",1163:"15A > IEC ADAPTER",1164:"13A > IEC JUMPER",1165:"16A > IEC ADAPTER",1166:"SOCA > IEC SPIDER",1167:"13A > SOCA SPIDER",1168:"TRELCO",1170:"15A > SOCA PLUG SPIDER",1171:"SOCA > 15A SOCKET SPIDER",1202:"13A IEC CABLE",1203:"15A IEC CABLE",1204:"16A IEC CABLE",1205:"GRELCO",1247:"15A > 32A ADAPTER",1248:"32A > 15A ADAPTER",1249:"32A > 16A ADAPTER",1256:"16A SPLITTER",1263:"32A > 16A RUBBER BOX",1264:"32A > IEC ADAPTER",1265:"13A > 32A ADAPTER",1266:"32A > 13A ADAPTER",1269:"SOCA SPLITTER BOX",1273:"IEC SPLITTER",1282:"13A EXTENSION",1288:"16A > TRUCON ADAPTER",1296:"16A > POWERCON ADAPTER",1297:"15A > TRUCON ADAPTER",1300:"110 V TRANSFORMER",1301:"DMX 8 WAY RELAY BOX",1304:"110 V SPLITTER",1305:"16A > 32A ADAPTER",1306:"TRUCON SPLITTER",1308:"13A > POWERCON",1309:"15A > POWERCON ADAPTER",3002:"POWERCON JOINER",3012:"13A > TRUCON ADAPTER",3013:"13A > C7 IEC (FIGURE 8)",3021:"TRUCON > 16A ADAPTER",3023:"16A > SOCA PLUG SPIDER",3024:"SOCA > 16A SOCKET SPIDER",3036:"13A > 110 V",3037:"110V > IEC",3038:"TRUCON > IEC",1001:"13A EXTENSION CABLE 4-WAY",1002:"13A EXTENSION REEL",1132:"15A TRS - 1m",1133:"15A TRS - 2m",1134:"15A TRS - 3m",1135:"15A TRS - 4m",1136:"15A TRS - 5m",1137:"15A TRS - 6m",1138:"15A TRS - 7m",1139:"15A TRS - 8m",1140:"15A TRS - 9m",1141:"15A TRS - 10m",1142:"15A TRS - 11m",1143:"15A TRS - 12m",1144:"15A TRS - 13m",1145:"15A TRS - 14m",1146:"15A TRS - 15m",1147:"15A TRS - 16m",1148:"15A TRS - 17m",1149:"15A TRS - 18m",1150:"15A TRS - 19m",1151:"15A TRS - 20m",1152:"15A TRS - 25m",1153:"15A TRS - 30m",1154:"15A TRS - 40m",1155:"15A TRS - 50m",1177:"16A TRS - 1m",1178:"16A TRS - 2m",1179:"16A TRS - 3m",1180:"16A TRS - 4m",1181:"16A TRS - 5m",1182:"16A TRS - 6m",1183:"16A TRS - 7m",1184:"16A TRS - 8m",1185:"16A TRS - 9m",1186:"16A TRS - 10m",1187:"16A TRS - 11m",1188:"16A TRS - 12m",1189:"16A TRS - 13m",1190:"16A TRS - 14m",1191:"16A TRS - 15m",1192:"16A TRS - 16m",1193:"16A TRS - 17m",1194:"16A TRS - 18m",1195:"16A TRS - 19m",1196:"16A TRS - 20m",1197:"16A TRS - 25m",1198:"16A TRS - 30m",1199:"16A TRS - 40m",1200:"16A TRS - 50m",1209:"SOCAPEX",1210:"IWB",1214:"SOCA - 3m",1215:"SOCA - 6m",1216:"SOCA - 8m",1217:"SOCA - 10m",1218:"SOCA - 12m",1219:"SOCA - 13m",1220:"SOCA - 15m",1221:"SOCA - 18m",1222:"SOCA - 20m",1223:"SOCA - 22m",1224:"SOCA - 25m",1225:"SOCA - 30m",1227:"32A - 30m",1228:"32A - 20m",1229:"32A - 15m",1230:"32A - 10m",1246:"SOCA - 2m",1267:"IEC CABLE",1287:"TRUCON EXTENSION - 1m",1295:"CABLE RETRACTOR",1303:"110 V EXTENSION",1307:"POWERCON EXTENSION",3003:"SOCA - 5m",3004:"SOCA - 7m",3005:"32A - 5m",3011:"KABUKI CABLE",3025:"TRUCON EXTENSION - 2m",3027:"TRUCON EXTENSION - 3m",3028:"TRUCON EXTENSION - 5m",3029:"TRUCON EXTENSION - 7m",3030:"TRUCON EXTENSION - 8m",3031:"TRUCON EXTENSION - 10m",3032:"TRUCON EXTENSION - 15m",3033:"TRUCON EXTENSION - 20m",3035:"IEC > 16A adapter ",1122:"STRAND 520 LIGHTING DESK",3034:"Lighting Desk",1005:"PORTABLE FLOOD LIGHT",1081:"PAR 64",1082:"AC 1000 FLOOD",1083:"LC9",1084:"PAR 64 - FLOOR CAN",1085:"STRAND PATT 243",1086:"STRAND PATT 123",1087:"STRAND PATT 23",1088:"STRAND PATT 743",1089:"AERO 4- WAY BATTEN",1090:"HOWIE BATTEN",1091:"500W SUN FLOOD",1092:"1000W SUN FLOOD",1093:"LED PAR CAN",1094:"ADB 1K FRESNEL",1095:"ADB 2K FRESNEL",1096:"CCT SIL 11 - 26",1097:"CCT SIL 15-32",1098:"CCT STARLETTE 1K FRESNEL",1099:"CCT STARLETTE 2K FRESNEL",1100:"ETC SOURCE 4 - 19",1101:"ETC SOURCE 4 - 26",1102:"ETC SOURCE 4 - 36",1103:"ETC SOURCE 4 - 10",1104:"ETC SOURCE 4 - 90",1105:"ETC SOURCE 4 ZOOM 15-30",1106:"ETC SOURCE 4 ZOOM 25-50",1107:"STRAND CANTATA 26-44",1108:"CCT SIL 30",1109:"CCT MINUETTE FRESNEL",1110:"CCT MINUETTE PC",1111:"CCT MINUETTE PROFILE",1112:"CCT MINUETTE FLOOD",1113:"JEM ZR 33 SMOKE MACHINE",1114:"JEM ZR 12 SMOKE MACHINE",1115:"UNIQUE HAZE MACHINE",1116:"SCROLLER PSU",1117:"AXIAL FAN",1118:"FESTOON",1119:"ROPE LIGHT",1120:"DMX SPLITTER",1121:"FOLLOWSPOT BALLAST",1125:"CCT STARLETTE 4 CELL FLOOD",1126:"CCT MINUETTE 4 CELL FLOOD",1128:"STRAND CANTATA 18-32",1129:"PINSPOT",1130:"BIRDIE - 240 V",1131:"BIRDIE TRANSFORMER",1162:"CLIP LIGHT",1206:"DIMMER",1211:"STRAND BAMBINO 5K",1212:"PAR 36 BEAN CAN",1213:"150W SUN FLOOD",1231:"ETC SOURCE 4 PAR",1250:"PAR 56",1251:"THOMAS FLOOD 4 CELL",1252:"THOMAS FLOOD 1 CELL",1253:"MIRRORBALL ROTATOR",1254:"THOMAS BATTEN",1255:"WAY 5+6 THOMAS BATTEN",1257:"PAR 38 BATTEN",1258:"STRAND 2K PC CADENZA",1259:"SNOW MACHINE",1260:"ATOMIC STROBE",1261:"DATAFLASH STROBE",1262:"SOUNDLAB SCANNER",1268:"SMOKE MACHINE",1270:"4 WAY DIMMER",1271:"SINGLE DIMMER",1272:"BLINDER",1275:"CCT SIL 15",1279:"INSPECTION LAMP",1280:"LED FLOOD",1281:"EMERGENCY LIGHT",1284:"ETC SOURCE 4 - 50",1286:"LED BIRDIE",1289:"SUNSTRIP",1290:"LED BATTEN",1291:"RAT STAND",1292:"UV LIGHT",1293:"BUBBLE MACHINE",1294:"CHAUVET VESUVIO",1298:"ETC SOURCE 4 - 14",1299:"LOW FOGGER",1302:"STRAND BEAM LIGHT",3000:"LE MAITRE MVS HAZER",3001:"CHAUVET CUMULUS",3006:"JEM AF1",3009:"PROLIGHT STUDIO COB",3022:"MARTIN MAC AURA XIP",3023:"ETC COLORSOURCE SPOT V",1006:"BATTERY CHARGER",1007:"FAN",1009:"BAR HEATER",1010:"FAN HEATER",1017:"ANGLEPOISE LAMP",1024:"HEATED CABINET",1025:"FRIDGE",1038:"ELECTRIC IRON",1046:"ELECTRIC GRINDER",1057:"MONITOR",1058:"PC",1059:"PRINTER",1060:"TV",1065:"VCR",1066:"AMPLIFIER",1071:"PROJECTOR",1078:"ELECTRIC DRILL",1201:"NETWORK SWITCH",1274:"WORKSHOP POWER TOOLS",1277:"POWER SUPPLY",1278:"RCD BLOCK",1283:"ELECTRO MAGNET",1285:"28 V TRANSFORMER",3007:"UNIVERSAL SERVO CONTROLLER",3008:"GLASSON PSU",3010:"KABUKI DROP",1172:"MIXER",1173:"PROCESSOR",1174:"PLAYBACK",1175:"COMPUTER",1176:"POWERED SPEAKER",1208:"IR SOURCE",3039:"13A > Klik",3040:"Klik > IEC",3041:"PowerCon > 110V",3042:"110V > 13A",3043:"PowerCon > IEC"}

    def importfromFluke(self, infile):
        self.fluke = flukeTest()
        dataout = self.fluke.parse(infile)
        for d in dataout:
            self.divice = {}
            id  = d['appno']
            print("Processing appliance with ID: " + id)
            if(id in self.Appliances):
                print("Duplicate ID: " + id)
                print("Existing appliance data: " + str(self.Appliances[id]))
                print("file_LOC: " + infile)
                print("testNum: " + d['testnum'])
                #input("Press enter to continue...")
            if(id == "0"):
                print("ID is 0, skipping...")
                continue
            self.divice['id'] = id
            self.divice['file'] = infile
            self.divice['user'] = d['user']
            self.divice['date'] = d['date']
            self.divice['testnum'] = d['testnum']
            self.divice['testmode'] = d['testmode']
            try:
                self.divice['itemtype'] = self.DiviceTypes[str(d['des1'])]["name"]
                self.divice['itemtype_ID'] = self.DiviceTypes[str(d['des1'])]["id"]
                self.divice['Type_ID'] = int(d['des1'])
            except:
                try:
                    lookup = "Unknown - " + d['des1']
                    if(lookup in self.outtableName):
                        #debug += "\nType found in outtableName, using previous value: " + str(self.outtableName[lookup])
                        #print("Type found in outtableName, using previous value: " + str(self.outtableName[lookup]))
                        self.divice['itemtype'] = lookup
                        self.divice['itemtype_ID'] = self.outtableName[lookup]["id"]
                        self.divice['Type_ID'] = self.outtableName[lookup]["number"]
                    else:
                        #debug += "\nUnknown Type found, attempting to learn: " + str(data[index])
                        #print("Unknown Type found, attempting to learn: " + str(data[index]))
                        self.divice['itemtype'] = "Unknown - " + d['des1']
                        self.divice['itemtype_ID'] = 1
                        self.divice['Type_ID'] = 1
                        print("Unknown Type found, attempting to learn: " + str(d['des1']))
                        #input("Press enter to continue...")
                except:
                    self.divice['itemtype'] = "Unknown"
                    self.divice['itemtype_ID'] = 1
                    self.divice['Type_ID'] = 1
            self.divice['location'] = d['loc']
            if(d['loc'] in self.Locations):
                self.divice["location_ID"] = self.Locations[d['loc']]
            else:
                self.divice["location_ID"] = 1
            dpass = True
            try:
                self.divice['Result'] = {"Visual": d['visual']}
                if(d['visual'] != "P"):
                    dpass = False
            except:
                self.divice['Result'] = {"Visual": "unknown"}
                dpass = False
            
            for t in d['tests']:
                #testtypes.append(t)
                self.divice['Result'][t] = {}
                if(t in self.testtypes):
                    pass
                else:
                    self.testtypes.append(t)
                #print(t)
                #print("-----")
                if(t in self.ListTypes):
                    pass
                else:
                    self.ListTypes[t] = []

                
                for k in d['tests'][t]:
                    self.divice['Result'][t][k] = d['tests'][t][k]
                    if(k == "pass"):
                        if(d['tests'][t][k] != "P"):
                            dpass = False

                    #print(f"{k}: {d['tests'][t][k]}")
                    if(k in self.ListTypes.get(t, [])):
                        pass
                    else:
                        self.ListTypes[t].append(k)
            #print(divice)

            #Divice overall result is pass if all tests are pass, otherwise fail. If any test is unknown, then overall result is fail
            if(dpass):
                self.divice['OverallResult'] = "Pass"
            else:
                self.divice['OverallResult'] = "Fail"

            #check for duplicate ID, if duplicate, add to dupes list, otherwise add to main list
            if(id in self.Appliances):
                print("Duplicate ID: " + id + " Adding to dupes list")
                print("Existing appliance data: " + str(self.Appliances[id]))
                # input("Press enter to continue...")

                self.dupesdiviceList[id] = self.divice
            else:
                self.Appliances[id] = self.divice
    def __get_Filedata(self, file):
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            Titles = next(reader)   # ✅ get first row
            data = next(reader)   # ✅ get first row
        return Titles, data
    def __storeData(self, divice, id, index, debug="", file_LOC=""):
        global counterApplianceNumber
        global duplicates
        global lastdisc
        global emptycount
        global debuglevel
        
        counterApplianceNumber += 1
        if(debuglevel > 0):
            print("\n\n-------------\nAppliance Number: " + str(self.data[index]) + "\nSaved!\n"+debug+"\n-------------")
        debug = ""
        if(debuglevel > 0):
            print("Next Appliance Found, resetting divice data...")
        if(str(int(id)) in self.Appliances):
            debug += "Duplicate ID found, skipping: " + str(id)
            divice["location"] = file_LOC
            if(file_LOC in self.Locations):
                divice["location_ID"] = self.Locations[file_LOC]
            else:
                divice["location_ID"] = 1
            self.dupesdiviceList[str(int(id))] = divice
            #print("Duplicate ID found, skipping: " + str(id))
            self.duplicates +=1
            self.dupes.append(id)
        else:
            if(divice != {}):
                #print(file_LOC)
                divice["location"] = ""
                divice["location"] = file_LOC
                if(file_LOC in self.Locations):
                    divice["location_ID"] = self.Locations[file_LOC]
                else:
                    divice["location_ID"] = 1
                #print(divice["location"])
                self.Appliances[str(int(id))] = divice
                #print("Appliance " + str(id) + ","+ str(int(id)) + " added to list with data: " + str(divice))
                self.lastdisc = index
                divice = {}
                #input("Press enter to continue...")
            else:
                debug += "No data found for appliance, skipping..."
                #print("No data found for appliance, skipping...")
                debug += "\nLast data point found at index: " + str(self.lastdisc)
                debug += "\nCurrent index: " + str(index)
                self.emptycount += 1
        return divice, debug
    def getfromFlukeSoftwere(self, infile):
        skip = 31
        debug = ""
        global counterApplianceNumber
        global duplicates
        global lastdisc
        global emptycount
        Titles, data = self.__get_Filedata(infile)
        #location 29th section in the data from lblClientInformation
        self.divice = {}
        id = 0
        stepname = "" 
        counter = 0
        file_LOC = data[28]
        for index, i in enumerate(Titles):
            if(counter < skip):
                counter += 1
                #continue

            match i:
                case "txtApplianceNumber":
                    self.divice, debug = self.__storeData(self.divice,id,index, debug, file_LOC=file_LOC)
                

                case "txtApplianceName":
                    try:
                        din = re.sub("[A-z]+", " ", data[index]).strip()
                        try:
                            int(din)
                        except ValueError:
                            debug += "\nNot a number found in Type field, attempting to learn..."
                            #print("Not a number found in Type field, attempting to learn...")
                            debug += "\n" + str(data[index])
                            #print(data[index])
                            if(data[index] in learned):
                                debug += "\nAlready learned, using previous value: " + str(learned[data[index]])
                                #print("Already learned, using previous value: " + str(learned[data[index]]))
                                din = learned[data[index]]
                            else:
                                dinx = din
                                print("Unlearned value found: " + str(dinx))
                                din = input("Enter a valid number for the Type field: ")
                                try:
                                    learn[data[index]] = int(din)
                                    learned[data[index]] = int(din)
                                    debug += "Learned " + str(dinx) + " as " + str(din)
                                except ValueError:
                                    debug += "\nNot a number, skipping..."
                                    #print("Not a number, skipping...")
                                    din = 0
                        self.divice['itemtype'] = self.DiviceTypes[str(din)]["name"]
                        self.divice['itemtype_ID'] = self.DiviceTypes[str(din)]["id"]
                        self.divice['Type_ID'] = int(din)
                    except KeyError:
                        lookup = "Unknown - " + data[index]
                        if(lookup in self.outtableName):
                            debug += "\nType found in outtableName, using previous value: " + str(self.outtableName[lookup])
                            #print("Type found in outtableName, using previous value: " + str(self.outtableName[lookup]))
                            self.divice['itemtype'] = lookup
                            self.divice['itemtype_ID'] = self.outtableName[lookup]["id"]
                            self.divice['Type_ID'] = self.outtableName[lookup]["number"]
                        else:
                            debug += "\nUnknown Type found, attempting to learn: " + str(data[index])
                            print("Unknown Type found, attempting to learn: " + str(data[index]))
                            #print("Unknown Type found, attempting to learn: " + str(data[index]))
                            self.divice['itemtype'] = "Unknown - " + data[index]
                            self.divice['itemtype_ID'] = 1
                            self.divice['Type_ID'] = 1
                            #input("Press enter to continue...")


            
                case "txtApplianceDate":#2026-04-26
                    month = data[index].split("-")[1]
                    year = data[index].split("-")[0]
                    day = data[index].split("-")[2]
                    if(year == "2026"):
                        year = "2025"
                    self.divice["date"] = year + "-" + month + "-" + day

                case "txtApplianceInterval":
                    self.divice["Interval"] = data[index]
                case "txtApplianceCode":
                    #counterApplianceNumber += 1
                    try:
                        id = int(data[index])
                    except ValueError:  
                        debug += "\nNot a number found in ID field, skipping..."
                        #print("Not a number found in ID field, skipping...")
                        id = data[index]
                        faild_ID.append(data[index])
                    if(id == "0"):
                        print("ID is 0, skipping...")
                        
                case "txtApplianceResult":
                    self.divice["OverallResult"] = data[index]
                case "txtTestStepName":
                    try:
                        self.divice["Result"][data[index]] = {}
                    except:
                        self.divice["Result"] = {}
                        self.divice["Result"][data[index]] = {}
                    #self.divice[data[index]] = {}
                    stepname = data[index]
                    if(data[index] not in self.testtypes):
                        print("New Test Type Found: " + data[index])
                        self.unknown_TestTypes.append(data[index])
                        self.testtypes.append(data[index])
                case "txtTestStepLimit":
                    self.divice["Result"][stepname]["Limit"] = data[index]
                case "txtTestStepMeasurement":
                    self.divice["Result"][stepname]["Measurement"] = data[index]
                case "txtTestStepResult":
                    self.divice["Result"][stepname]["Result"] = data[index]
                    
                case "txtFailedAppliances":
                    global fialed_appl
                    fialed_appl += int(data[index])
                case "txtPassedAppliances":
                    global passed_appl
                    passed_appl += int(data[index])
                case i if i in ignore_Types:
                    debug += "\nType is in the ignore list: " + i
                    #print("Ignoring " + i)
                case _:
                    debug += "\nUnhandled data point found: " + i + " with value: " + str(data[index])
                    #print("Not Found")
                    #print(i)
                    #print(data[index])
                    if(i in unhandled):
                        debug += "\nAlready marked as unhandled, skipping..."
                    else:                    
                        unhandled.append(i)
                    #print("-------------")
        
        # Store the final appliance after loop completes
        self.divice, debug = self.__storeData(self.divice, id, len(Titles)-1, debug, file_LOC=file_LOC)
    def getlistofFiles(self, path):
        import os
        
        for r, d, f in os.walk(path):
            for file in f:
                if '.csv' in file:
                    self.csv.append(os.path.join(r, file))
                if '.FLK' in file:
                    self.fluke.append(os.path.join(r, file))
    def processFiles(self,file_LOC):
        self.getlistofFiles(file_LOC)
        if(len(self.fluke) == 0 and len(self.csv) == 0):
            print("No files found in the specified location.")
            return
        elif(len(self.fluke) == 0):
            print("No Fluke files found, processing CSV files only...")
            for c in self.csv:
                self.getfromFlukeSoftwere(c)
        elif(len(self.csv) == 0):
            print("No CSV files found, processing Fluke files only...")
            for f in self.fluke:
                print(f"Processing Fluke file: {f}")
                self.importfromFluke(f)
        else:
            print(f"Found {len(self.fluke)} Fluke files and {len(self.csv)} CSV files, processing all files...")
            for f in self.fluke:
                self.importfromFluke(f)
            for c in self.csv:
                self.getfromFlukeSoftwere(c)
    def snipeITData(self):
        self.Appliances = self.fixDates(self.Appliances)
        self.dupesdiviceList = self.fixDates(self.dupesdiviceList)
        #self.exporttoCSV()
        self.sendtosnipe()
        Maintcounter = self.maintenanceCreate()
        print("Total Appliances Processed: " + str(len(self.Appliances)))
        print("Total Dupe Processed: " + str(len(self.dupesdiviceList)))
        print("Total Maintenances Created: " + str(Maintcounter))

    
    def fixDates(self, appliances=None):
        if appliances is None:
            appliances = self.Appliances
        for a in appliances:
            if(a == 0):
                continue
            print(f"Processing appliance {a} for date fix...")
            try:
                appliances[a]['date']  =  (datetime.datetime.strptime(appliances[a]['date'], "%d-%b-%y")).strftime("%Y-%m-%d")
                nextdate = (datetime.datetime.strptime(appliances[a]['date'], "%d-%b-%y") + datetime.timedelta(days=365)).strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Error processing date for appliance {a}: {e}")
                nextdate = str(int(appliances[a]['date'].split('-')[0]) + 1) + "-" + appliances[a]['date'].split('-')[1] + "-" + str(int(appliances[a]['date'].split('-')[2]))
            appliances[a]['nextdate'] = nextdate

        return appliances
    def exporttoCSV(self, outfile="Output.csv"):

        #Asset Tag,Model Name,Next Audit Date,PatTest_Result,Location
        output = "Asset Tag,Item Name,Model Name,Next Audit Date,PatTest_Result,Location\n"
        for a in self.Appliances:
            if(a == 0):
                continue
            print(f"Processing appliance {a} for export...")
            output += f"{a},{a},{self.Appliances[a]['itemtype']},{self.Appliances[a]['nextdate']},{self.Appliances[a]['OverallResult']},{self.Appliances[a]['location']}\n"

        with open(outfile, "w") as f:
            f.write(output)

#### Import CSV to SnipeIT
    def sendtosnipe(self, infile="Output.csv"):
        for a in self.Appliances:
            if(a == 0):
                continue
            print(f"Processing appliance {a} for SnipeIT...")
            self.snipeassetSend(a)
    
    def snipeassetSend(self,a, retry=0):
        try:
            if(self.assets[a] != None):
                print(f"Appliance {a} already exists in SnipeIT with ID {self.assets[str(a)]['id']}, skipping...")
                if(self.assets[str(a)]['model'] != self.Appliances[str(a)]['itemtype_ID']):
                    print(f"Model mismatch for appliance {a}, updating model in SnipeIT...")
                    print(updateAssetModdel(self.snipeITUrl,self.apiKey, self.assets[str(a)]['id'], self.Appliances[str(a)]['itemtype_ID'], a))
                return 1
        except KeyError:
            
            print(f"Appliance {a} not found in SnipeIT, creating new entry...")
            print(type(a))
            data = json.loads(createAsset(self.snipeITUrl, self.apiKey, self.Appliances[a], a))
            if(data["status"] == "error"):
                print(f"Error creating appliance {a} in SnipeIT: {data['messages']} moddel ID: {self.Appliances[a]['itemtype_ID']}")
                input("Press enter to continue try again...")
                retry += 1
                if(retry < 3):
                    return 3
                else:
                    self.snipeassetSend(a, retry)
                return 3
            return 2
        
    def maintenanceCreate(self):
        from SnipeAsset.Update import update_SnipeIT
        Maintcounter = 0
        print(f"Creating maintenance for appliances...")
        Maintcounter = update_SnipeIT(self.Appliances, self.testtypes,self.snipeITUrl,self.apiKey)
        # Skip maintenance for duplicates to avoid duplicate data
        # Maintcounter += update_SnipeIT(self.dupesdiviceList, self.testtypes,self.snipeITUrl,self.apiKey)
        return Maintcounter