#/bin/python3
DiviceTypes = {1156:"13A > 15A ADAPTER",1157:"15A > 13A ADAPTER",1158:"13A > 16A ADAPTER",1159:"16A > 13A ADAPTER",1160:"16A > 15A ADAPTER",1161:"15A > 16A ADAPTER",1163:"15A > IEC ADAPTER",1164:"13A > IEC JUMPER",1165:"16A > IEC ADAPTER",1166:"SOCA > IEC SPIDER",1167:"13A > SOCA SPIDER",1168:"TRELCO",1170:"15A > SOCA PLUG SPIDER",1171:"SOCA > 15A SOCKET SPIDER",1202:"13A IEC CABLE",1203:"15A IEC CABLE",1204:"16A IEC CABLE",1205:"GRELCO",1247:"15A > 32A ADAPTER",1248:"32A > 15A ADAPTER",1249:"32A > 16A ADAPTER",1256:"16A SPLITTER",1263:"32A > 16A RUBBER BOX",1264:"32A > IEC ADAPTER",1265:"13A > 32A ADAPTER",1266:"32A > 13A ADAPTER",1269:"SOCA SPLITTER BOX",1273:"IEC SPLITTER",1282:"13A EXTENSION",1288:"16A > TRUCON ADAPTER",1296:"16A > POWERCON ADAPTER",1297:"15A > TRUCON ADAPTER",1300:"110 V TRANSFORMER",1301:"DMX 8 WAY RELAY BOX",1304:"110 V SPLITTER",1305:"16A > 32A ADAPTER",1306:"TRUCON SPLITTER",1308:"13A > POWERCON",1309:"15A > POWERCON ADAPTER",3002:"POWERCON JOINER",3012:"13A > TRUCON ADAPTER",3013:"13A > C7 IEC (FIGURE 8)",3021:"TRUCON > 16A ADAPTER",3023:"16A > SOCA PLUG SPIDER",3024:"SOCA > 16A SOCKET SPIDER",3036:"13A > 110 V",3037:"110V > IEC",3038:"TRUCON > IEC",1001:"13A EXTENSION CABLE 4-WAY",1002:"13A EXTENSION REEL",1132:"15A TRS - 1m",1133:"15A TRS - 2m",1134:"15A TRS - 3m",1135:"15A TRS - 4m",1136:"15A TRS - 5m",1137:"15A TRS - 6m",1138:"15A TRS - 7m",1139:"15A TRS - 8m",1140:"15A TRS - 9m",1141:"15A TRS - 10m",1142:"15A TRS - 11m",1143:"15A TRS - 12m",1144:"15A TRS - 13m",1145:"15A TRS - 14m",1146:"15A TRS - 15m",1147:"15A TRS - 16m",1148:"15A TRS - 17m",1149:"15A TRS - 18m",1150:"15A TRS - 19m",1151:"15A TRS - 20m",1152:"15A TRS - 25m",1153:"15A TRS - 30m",1154:"15A TRS - 40m",1155:"15A TRS - 50m",1177:"16A TRS - 1m",1178:"16A TRS - 2m",1179:"16A TRS - 3m",1180:"16A TRS - 4m",1181:"16A TRS - 5m",1182:"16A TRS - 6m",1183:"16A TRS - 7m",1184:"16A TRS - 8m",1185:"16A TRS - 9m",1186:"16A TRS - 10m",1187:"16A TRS - 11m",1188:"16A TRS - 12m",1189:"16A TRS - 13m",1190:"16A TRS - 14m",1191:"16A TRS - 15m",1192:"16A TRS - 16m",1193:"16A TRS - 17m",1194:"16A TRS - 18m",1195:"16A TRS - 19m",1196:"16A TRS - 20m",1197:"16A TRS - 25m",1198:"16A TRS - 30m",1199:"16A TRS - 40m",1200:"16A TRS - 50m",1209:"SOCAPEX",1210:"IWB",1214:"SOCA - 3m",1215:"SOCA - 6m",1216:"SOCA - 8m",1217:"SOCA - 10m",1218:"SOCA - 12m",1219:"SOCA - 13m",1220:"SOCA - 15m",1221:"SOCA - 18m",1222:"SOCA - 20m",1223:"SOCA - 22m",1224:"SOCA - 25m",1225:"SOCA - 30m",1227:"32A - 30m",1228:"32A - 20m",1229:"32A - 15m",1230:"32A - 10m",1246:"SOCA - 2m",1267:"IEC CABLE",1287:"TRUCON EXTENSION - 1m",1295:"CABLE RETRACTOR",1303:"110 V EXTENSION",1307:"POWERCON EXTENSION",3003:"SOCA - 5m",3004:"SOCA - 7m",3005:"32A - 5m",3011:"KABUKI CABLE",3025:"TRUCON EXTENSION - 2m",3027:"TRUCON EXTENSION - 3m",3028:"TRUCON EXTENSION - 5m",3029:"TRUCON EXTENSION - 7m",3030:"TRUCON EXTENSION - 8m",3031:"TRUCON EXTENSION - 10m",3032:"TRUCON EXTENSION - 15m",3033:"TRUCON EXTENSION - 20m",3035:"IEC > 16A adapter ",1122:"STRAND 520 LIGHTING DESK",3034:"Lighting Desk",1005:"PORTABLE FLOOD LIGHT",1081:"PAR 64",1082:"AC 1000 FLOOD",1083:"LC9",1084:"PAR 64 - FLOOR CAN",1085:"STRAND PATT 243",1086:"STRAND PATT 123",1087:"STRAND PATT 23",1088:"STRAND PATT 743",1089:"AERO 4- WAY BATTEN",1090:"HOWIE BATTEN",1091:"500W SUN FLOOD",1092:"1000W SUN FLOOD",1093:"LED PAR CAN",1094:"ADB 1K FRESNEL",1095:"ADB 2K FRESNEL",1096:"CCT SIL 11 - 26",1097:"CCT SIL 15-32",1098:"CCT STARLETTE 1K FRESNEL",1099:"CCT STARLETTE 2K FRESNEL",1100:"ETC SOURCE 4 - 19",1101:"ETC SOURCE 4 - 26",1102:"ETC SOURCE 4 - 36",1103:"ETC SOURCE 4 - 10",1104:"ETC SOURCE 4 - 90",1105:"ETC SOURCE 4 ZOOM 15-30",1106:"ETC SOURCE 4 ZOOM 25-50",1107:"STRAND CANTATA 26-44",1108:"CCT SIL 30",1109:"CCT MINUETTE FRESNEL",1110:"CCT MINUETTE PC",1111:"CCT MINUETTE PROFILE",1112:"CCT MINUETTE FLOOD",1113:"JEM ZR 33 SMOKE MACHINE",1114:"JEM ZR 12 SMOKE MACHINE",1115:"UNIQUE HAZE MACHINE",1116:"SCROLLER PSU",1117:"AXIAL FAN",1118:"FESTOON",1119:"ROPE LIGHT",1120:"DMX SPLITTER",1121:"FOLLOWSPOT BALLAST",1125:"CCT STARLETTE 4 CELL FLOOD",1126:"CCT MINUETTE 4 CELL FLOOD",1128:"STRAND CANTATA 18-32",1129:"PINSPOT",1130:"BIRDIE - 240 V",1131:"BIRDIE TRANSFORMER",1162:"CLIP LIGHT",1206:"DIMMER",1211:"STRAND BAMBINO 5K",1212:"PAR 36 BEAN CAN",1213:"150W SUN FLOOD",1231:"ETC SOURCE 4 PAR",1250:"PAR 56",1251:"THOMAS FLOOD 4 CELL",1252:"THOMAS FLOOD 1 CELL",1253:"MIRRORBALL ROTATOR",1254:"THOMAS BATTEN",1255:"WAY 5+6 THOMAS BATTEN",1257:"PAR 38 BATTEN",1258:"STRAND 2K PC CADENZA",1259:"SNOW MACHINE",1260:"ATOMIC STROBE",1261:"DATAFLASH STROBE",1262:"SOUNDLAB SCANNER",1268:"SMOKE MACHINE",1270:"4 WAY DIMMER",1271:"SINGLE DIMMER",1272:"BLINDER",1275:"CCT SIL 15",1279:"INSPECTION LAMP",1280:"LED FLOOD",1281:"EMERGENCY LIGHT",1284:"ETC SOURCE 4 - 50",1286:"LED BIRDIE",1289:"SUNSTRIP",1290:"LED BATTEN",1291:"RAT STAND",1292:"UV LIGHT",1293:"BUBBLE MACHINE",1294:"CHAUVET VESUVIO",1298:"ETC SOURCE 4 - 14",1299:"LOW FOGGER",1302:"STRAND BEAM LIGHT",3000:"LE MAITRE MVS HAZER",3001:"CHAUVET CUMULUS",3006:"JEM AF1",3009:"PROLIGHT STUDIO COB",3022:"MARTIN MAC AURA XIP",3023:"ETC COLORSOURCE SPOT V",1006:"BATTERY CHARGER",1007:"FAN",1009:"BAR HEATER",1010:"FAN HEATER",1017:"ANGLEPOISE LAMP",1024:"HEATED CABINET",1025:"FRIDGE",1038:"ELECTRIC IRON",1046:"ELECTRIC GRINDER",1057:"MONITOR",1058:"PC",1059:"PRINTER",1060:"TV",1065:"VCR",1066:"AMPLIFIER",1071:"PROJECTOR",1078:"ELECTRIC DRILL",1201:"NETWORK SWITCH",1274:"WORKSHOP POWER TOOLS",1277:"POWER SUPPLY",1278:"RCD BLOCK",1283:"ELECTRO MAGNET",1285:"28 V TRANSFORMER",3007:"UNIVERSAL SERVO CONTROLLER",3008:"GLASSON PSU",3010:"KABUKI DROP",1172:"MIXER",1173:"PROCESSOR",1174:"PLAYBACK",1175:"COMPUTER",1176:"POWERED SPEAKER",1208:"IR SOURCE",3039:"13A > Klik",3040:"Klik > IEC",3041:"PowerCon > 110V",3042:"110V > 13A",3043:"PowerCon > IEC"}
from Update import *
import json
import requests
import csv
import re
from os import system
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
from csvimport import addCSV
requestcounter = 0

def get_Filedata(file):
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        Titles = next(reader)   # ✅ get first row
        data = next(reader)   # ✅ get first row
    return Titles, data

#data = csv.reader(data)

#data = list(data)
#data = data.split(",")
#Titles = Titles.split(",")
TypesofTest = ['VISUAL', 'RPE', 'RINS', 'L,N-condition', 'IPE', 'FUNCTION']
#exit()
diviceList = {}
dupesdiviceList = {}
lastdisc = 0

def storeData(divice,id, index, debug="", file_LOC=""):
    global counterApplianceNumber
    global duplicates
    global lastdisc
    global emptycount
    global debuglevel
    global diviceList
    counterApplianceNumber += 1
    if(debuglevel > 0):
        print("\n\n-------------\nAppliance Number: " + str(data[index]) + "\nSaved!\n"+debug+"\n-------------")
    debug = ""
    if(debuglevel > 0):
        print("Next Appliance Found, resetting divice data...")
    if(str(int(id)) in diviceList):
        debug += "Duplicate ID found, skipping: " + str(id)
        divice["location"] = file_LOC
        dupesdiviceList[str(int(id))] = divice
        #print("Duplicate ID found, skipping: " + str(id))
        duplicates +=1
        dupes.append(id)
    if(divice != {}):
        #print(file_LOC)
        divice["location"] = ""
        divice["location"] = file_LOC
        #print(divice["location"])
        diviceList[str(int(id))] = divice
        #print("Appliance " + str(id) + ","+ str(int(id)) + " added to list with data: " + str(divice))
        lastdisc = index
        divice = {}
        #input("Press enter to continue...")
    else:
        debug += "No data found for appliance, skipping..."
        #print("No data found for appliance, skipping...")
        debug += "\nLast data point found at index: " + str(lastdisc)
        debug += "\nCurrent index: " + str(index)
        emptycount += 1
    return divice, debug

def dealWithData(file):
    debug = ""
    global counterApplianceNumber
    global duplicates
    global lastdisc
    global emptycount
    Titles, data = get_Filedata(file)
    #location 29th section in the data from lblClientInformation
    divice = {}
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
                divice, debug = storeData(divice,id,index, debug, file_LOC=file_LOC)
            

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
                    divice["Type_ID"] = din
                    divice["Type"] = DiviceTypes[int(din)]
                except KeyError:
                    divice["Type"] = "Unknown - " + data[index]
            case "txtApplianceDate":#2026-04-26
                month = data[index].split("-")[1]
                year = data[index].split("-")[0]
                day = data[index].split("-")[2]
                if(year == "2026"):
                    year = "2025"
                divice["Date"] = year + "-" + month + "-" + day

            case "txtApplianceInterval":
                divice["Interval"] = data[index]
            case "txtApplianceCode":
                #counterApplianceNumber += 1
                try:
                    id = int(data[index])
                except ValueError:  
                    debug += "\nNot a number found in ID field, skipping..."
                    #print("Not a number found in ID field, skipping...")
                    id = data[index]
                    faild_ID.append(data[index])
            case "txtApplianceResult":
                divice["Result"] = data[index]
            case "txtTestStepName":
                divice[data[index]] = {}
                stepname = data[index]
                if(data[index] not in TypesofTest):
                    print("New Test Type Found: " + data[index])
                    unknown_TestTypes.append(data[index])
                    TypesofTest.append(data[index])
            case "txtTestStepLimit":
                divice[stepname]["Limit"] = data[index]
            case "txtTestStepMeasurement":
                divice[stepname]["Measurement"] = data[index]
            case "txtTestStepResult":
                divice[stepname]["Result"] = data[index]
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
    divice, debug = storeData(divice,id,index, debug, file_LOC=file_LOC)
#input("Press enter to start processing data...")
print("Removing old files list and making new files list")
print(system("rm test.txt"))
print(system("ls ../reports >> test.txt"))
print("Processing: ")
#out = ""
with open("test.txt", "r") as file:
    data = file.read()
    print(data.split("\n"))

input("Press enter to continue....")

with open("test.txt", "r") as file:
    data = file.read()
    for line in data.split("\n"):
        if(line != ""):
            print("../reports/"+line)

            dealWithData("../reports/"+line)

#input("Data processing complete, press enter to see results...")
#print(diviceList)
if(outattheend == 1):
    print("-------------\nData processing complete!\n----------")
    print("Total diviceList length: " + str(len(diviceList)+len(dupesdiviceList)))
    print("Test Types found: " + str(TypesofTest))
    print("Unknown Test Types found: " + str(unknown_TestTypes))
    print("Passed Appliances: " + str(passed_appl))
    print("Failed Appliances: " + str(fialed_appl))
    print("Duplicates Found: " + str(dupes))
    print("Unhandled Data Points: " + str(unhandled))
    print("Failed IDs: " + str(faild_ID))
    print("duplicates: " + str(duplicates))
    print("empty lines: " + str(emptycount))
    print("CounterApplianceNumber: " + str(counterApplianceNumber))
    print("---------\n pls add the below to the learnd vallues\n")
    print(learn)
    
print("Saving Data to Export.csv")

#Export Assets to CSV:
out = "Asset Tag,Model Name,Next Audit Date,Last Audit,PatTest_Result,Location\n"
for i in diviceList:
    divice = diviceList[i]
    #divice["Date"] = '2025-08-28'
    Nextdate = str(int(divice["Date"].split('-')[0]) + 1) + "-" + divice["Date"].split('-')[1] + "-" + divice["Date"].split('-')[2]
    out += str(i) + "," + divice["Type"] + "," + Nextdate + ',' + divice["Date"] + "," + divice["Result"] + "," + divice["location"] + "\n"

with open("Export.csv", "w") as file:
    file.write(out)

print("Atempting to upload to Snipe it:")
print(system("./Upload.sh"))

print("Storing all data in output.csv for Local Use.")
#Output Table data for fun:

outputdata = 'ID,Type,Type_ID,Location,Date,Interval,Result,VISUAL Limit,VISUAL Measurement,VISUAL Result,RPE Limit,RPE Measurement,RPE Result,RINS Limit,RINS Measurement,RINS Result,"L,N-condition" Limit,"L,N-condition" Measurement,"L,N-condition" Result,IPE Limit,IPE Measurement,IPE Result,FUNCTION Limit,FUNCTION Measurement,FUNCTION Result\n'


def make_CSVData(diviceList):
    global TypesofTest
    outputdata = ""
    for i in diviceList:
        divice = diviceList[i]
        try:
            divice["location"]
            #print(divice["location"])
        except KeyError:
            print("No location found for divice " + str(i) + ", Fixing...")
            divice["location"] = "Nofound"
        
        outputdata += str(i) + "," + divice["Type"] + "," + str(divice["Type_ID"]) + "," + str(divice["location"]) + " ," + divice["Date"] + "," + divice["Interval"] + "," + divice["Result"]
        for test in TypesofTest:
            try:
                #print(divice[test])
                outputdata += "," + divice[test]["Limit"]
                outputdata += "," + divice[test]["Measurement"]
                outputdata += "," + divice[test]["Result"]
            except KeyError:
                outputdata += ",No Data, No Data, No Data"

                #print("Not Found")
        outputdata += "\n"
    return outputdata

outputdata += make_CSVData(diviceList)
outputdata += make_CSVData(dupesdiviceList)

with open("output.csv", "w") as file:
    file.write(outputdata)

print(TypesofTest)
input("Exported data to Export.csv, Upload to Snipe-IT and press enter to continue...")


#Data to export:    txtApplianceNumber,txtApplianceName,txtApplianceDate,txtApplianceInterval,,txtApplianceCode,txtApplianceResult,txtTestStepName,txtTestStepLimit,txtTestStepMeasurement,txtTestStepResult,txtTestStepName,txtTestStepLimit,txtTestStepMeasurement,txtTestStepResult,txtTestStepName,txtTestStepLimit,txtTestStepMeasurement,txtTestStepResult,txtTestStepName,txtTestStepLimit,txtTestStepMeasurement,txtTestStepResult,txtTestStepName,txtTestStepLimit,txtTestStepMeasurement,txtTestStepResult,
#                                      1130,            2026-04-26,      12M,                , 4635,           Passed,             VISUAL,        -,               [OK],                  Passed,           RPE,            ≤ 0.3,           [0.03 OHM],            Passed,           RINS,           ≥ 1.0,           [>299 MOHM],           Passed,           IPE,              ≤ 3.5,          [0.05 mA],       Passed,                FUNCTION,         ≤ 3000,         [2 VA],               Passed,

print("Data Processed, now updating Snipe-IT with pat-Test data...")
#Visual:
#Limit "-" - Measurement [OK] - Result Passed

# '4585': {'Type': '13A > IEC JUMPER', 'Date': '2026-04-26', 'Interval': '12M', 'Result': 'Passed', 'VISUAL': {'Limit': ' -', 'Measurement': '[OK]', 'Result': 'Passed'}, 'RPE': {'Limit': ' ≤ 0.2', 'Measurement': '[0.03 OHM]', 'Result': 'Passed'}, 'RINS': {'Limit': ' ≥ 1.0', 'Measurement': '[>299 MOHM]', 'Result': 'Passed'}, '"LN-condition"': {'Limit': ' -', 'Measurement': '[OK]', 'Result': 'Passed'}}

#Send data to API:

outData = ""
def update_SnipeIT(diviceList):

    for i in diviceList:
        print("-----------\nWorking on " + i + ": ")
        outData = ""
        divice = diviceList[i]
        for test in TypesofTest:
            try:
                divice[test]
                #print(divice[test])
                outData += test
                outData += " - Limit: " + divice[test]["Limit"]
                outData += " - Measurement: " + divice[test]["Measurement"]
                outData += " - Result: " + divice[test]["Result"]
                outData += "\n"
                #print(outData)
            except KeyError:
                outData += test + " - No Data\n"
                #print("Test: "+ test + " Not Found! Applying No Data")
                #print("Not Found")
        print("Updating Snipe-IT ID: " + i + "  and date: " + divice["Date"] + " with the following data:\n" + outData)
        #print(divice["Date"])
        Update(i, outData, divice["Date"])



update_SnipeIT(diviceList)
update_SnipeIT(dupesdiviceList)
