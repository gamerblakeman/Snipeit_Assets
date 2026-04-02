from FlukeDMS import flukeTest
import json
import datetime
test = flukeTest()

dataout = test.parse("123.FLK")

print(dataout[1])

DiviceTypes = {1156:"13A > 15A ADAPTER",1157:"15A > 13A ADAPTER",1158:"13A > 16A ADAPTER",1159:"16A > 13A ADAPTER",1160:"16A > 15A ADAPTER",1161:"15A > 16A ADAPTER",1163:"15A > IEC ADAPTER",1164:"13A > IEC JUMPER",1165:"16A > IEC ADAPTER",1166:"SOCA > IEC SPIDER",1167:"13A > SOCA SPIDER",1168:"TRELCO",1170:"15A > SOCA PLUG SPIDER",1171:"SOCA > 15A SOCKET SPIDER",1202:"13A IEC CABLE",1203:"15A IEC CABLE",1204:"16A IEC CABLE",1205:"GRELCO",1247:"15A > 32A ADAPTER",1248:"32A > 15A ADAPTER",1249:"32A > 16A ADAPTER",1256:"16A SPLITTER",1263:"32A > 16A RUBBER BOX",1264:"32A > IEC ADAPTER",1265:"13A > 32A ADAPTER",1266:"32A > 13A ADAPTER",1269:"SOCA SPLITTER BOX",1273:"IEC SPLITTER",1282:"13A EXTENSION",1288:"16A > TRUCON ADAPTER",1296:"16A > POWERCON ADAPTER",1297:"15A > TRUCON ADAPTER",1300:"110 V TRANSFORMER",1301:"DMX 8 WAY RELAY BOX",1304:"110 V SPLITTER",1305:"16A > 32A ADAPTER",1306:"TRUCON SPLITTER",1308:"13A > POWERCON",1309:"15A > POWERCON ADAPTER",3002:"POWERCON JOINER",3012:"13A > TRUCON ADAPTER",3013:"13A > C7 IEC (FIGURE 8)",3021:"TRUCON > 16A ADAPTER",3023:"16A > SOCA PLUG SPIDER",3024:"SOCA > 16A SOCKET SPIDER",3036:"13A > 110 V",3037:"110V > IEC",3038:"TRUCON > IEC",1001:"13A EXTENSION CABLE 4-WAY",1002:"13A EXTENSION REEL",1132:"15A TRS - 1m",1133:"15A TRS - 2m",1134:"15A TRS - 3m",1135:"15A TRS - 4m",1136:"15A TRS - 5m",1137:"15A TRS - 6m",1138:"15A TRS - 7m",1139:"15A TRS - 8m",1140:"15A TRS - 9m",1141:"15A TRS - 10m",1142:"15A TRS - 11m",1143:"15A TRS - 12m",1144:"15A TRS - 13m",1145:"15A TRS - 14m",1146:"15A TRS - 15m",1147:"15A TRS - 16m",1148:"15A TRS - 17m",1149:"15A TRS - 18m",1150:"15A TRS - 19m",1151:"15A TRS - 20m",1152:"15A TRS - 25m",1153:"15A TRS - 30m",1154:"15A TRS - 40m",1155:"15A TRS - 50m",1177:"16A TRS - 1m",1178:"16A TRS - 2m",1179:"16A TRS - 3m",1180:"16A TRS - 4m",1181:"16A TRS - 5m",1182:"16A TRS - 6m",1183:"16A TRS - 7m",1184:"16A TRS - 8m",1185:"16A TRS - 9m",1186:"16A TRS - 10m",1187:"16A TRS - 11m",1188:"16A TRS - 12m",1189:"16A TRS - 13m",1190:"16A TRS - 14m",1191:"16A TRS - 15m",1192:"16A TRS - 16m",1193:"16A TRS - 17m",1194:"16A TRS - 18m",1195:"16A TRS - 19m",1196:"16A TRS - 20m",1197:"16A TRS - 25m",1198:"16A TRS - 30m",1199:"16A TRS - 40m",1200:"16A TRS - 50m",1209:"SOCAPEX",1210:"IWB",1214:"SOCA - 3m",1215:"SOCA - 6m",1216:"SOCA - 8m",1217:"SOCA - 10m",1218:"SOCA - 12m",1219:"SOCA - 13m",1220:"SOCA - 15m",1221:"SOCA - 18m",1222:"SOCA - 20m",1223:"SOCA - 22m",1224:"SOCA - 25m",1225:"SOCA - 30m",1227:"32A - 30m",1228:"32A - 20m",1229:"32A - 15m",1230:"32A - 10m",1246:"SOCA - 2m",1267:"IEC CABLE",1287:"TRUCON EXTENSION - 1m",1295:"CABLE RETRACTOR",1303:"110 V EXTENSION",1307:"POWERCON EXTENSION",3003:"SOCA - 5m",3004:"SOCA - 7m",3005:"32A - 5m",3011:"KABUKI CABLE",3025:"TRUCON EXTENSION - 2m",3027:"TRUCON EXTENSION - 3m",3028:"TRUCON EXTENSION - 5m",3029:"TRUCON EXTENSION - 7m",3030:"TRUCON EXTENSION - 8m",3031:"TRUCON EXTENSION - 10m",3032:"TRUCON EXTENSION - 15m",3033:"TRUCON EXTENSION - 20m",3035:"IEC > 16A adapter ",1122:"STRAND 520 LIGHTING DESK",3034:"Lighting Desk",1005:"PORTABLE FLOOD LIGHT",1081:"PAR 64",1082:"AC 1000 FLOOD",1083:"LC9",1084:"PAR 64 - FLOOR CAN",1085:"STRAND PATT 243",1086:"STRAND PATT 123",1087:"STRAND PATT 23",1088:"STRAND PATT 743",1089:"AERO 4- WAY BATTEN",1090:"HOWIE BATTEN",1091:"500W SUN FLOOD",1092:"1000W SUN FLOOD",1093:"LED PAR CAN",1094:"ADB 1K FRESNEL",1095:"ADB 2K FRESNEL",1096:"CCT SIL 11 - 26",1097:"CCT SIL 15-32",1098:"CCT STARLETTE 1K FRESNEL",1099:"CCT STARLETTE 2K FRESNEL",1100:"ETC SOURCE 4 - 19",1101:"ETC SOURCE 4 - 26",1102:"ETC SOURCE 4 - 36",1103:"ETC SOURCE 4 - 10",1104:"ETC SOURCE 4 - 90",1105:"ETC SOURCE 4 ZOOM 15-30",1106:"ETC SOURCE 4 ZOOM 25-50",1107:"STRAND CANTATA 26-44",1108:"CCT SIL 30",1109:"CCT MINUETTE FRESNEL",1110:"CCT MINUETTE PC",1111:"CCT MINUETTE PROFILE",1112:"CCT MINUETTE FLOOD",1113:"JEM ZR 33 SMOKE MACHINE",1114:"JEM ZR 12 SMOKE MACHINE",1115:"UNIQUE HAZE MACHINE",1116:"SCROLLER PSU",1117:"AXIAL FAN",1118:"FESTOON",1119:"ROPE LIGHT",1120:"DMX SPLITTER",1121:"FOLLOWSPOT BALLAST",1125:"CCT STARLETTE 4 CELL FLOOD",1126:"CCT MINUETTE 4 CELL FLOOD",1128:"STRAND CANTATA 18-32",1129:"PINSPOT",1130:"BIRDIE - 240 V",1131:"BIRDIE TRANSFORMER",1162:"CLIP LIGHT",1206:"DIMMER",1211:"STRAND BAMBINO 5K",1212:"PAR 36 BEAN CAN",1213:"150W SUN FLOOD",1231:"ETC SOURCE 4 PAR",1250:"PAR 56",1251:"THOMAS FLOOD 4 CELL",1252:"THOMAS FLOOD 1 CELL",1253:"MIRRORBALL ROTATOR",1254:"THOMAS BATTEN",1255:"WAY 5+6 THOMAS BATTEN",1257:"PAR 38 BATTEN",1258:"STRAND 2K PC CADENZA",1259:"SNOW MACHINE",1260:"ATOMIC STROBE",1261:"DATAFLASH STROBE",1262:"SOUNDLAB SCANNER",1268:"SMOKE MACHINE",1270:"4 WAY DIMMER",1271:"SINGLE DIMMER",1272:"BLINDER",1275:"CCT SIL 15",1279:"INSPECTION LAMP",1280:"LED FLOOD",1281:"EMERGENCY LIGHT",1284:"ETC SOURCE 4 - 50",1286:"LED BIRDIE",1289:"SUNSTRIP",1290:"LED BATTEN",1291:"RAT STAND",1292:"UV LIGHT",1293:"BUBBLE MACHINE",1294:"CHAUVET VESUVIO",1298:"ETC SOURCE 4 - 14",1299:"LOW FOGGER",1302:"STRAND BEAM LIGHT",3000:"LE MAITRE MVS HAZER",3001:"CHAUVET CUMULUS",3006:"JEM AF1",3009:"PROLIGHT STUDIO COB",3022:"MARTIN MAC AURA XIP",3023:"ETC COLORSOURCE SPOT V",1006:"BATTERY CHARGER",1007:"FAN",1009:"BAR HEATER",1010:"FAN HEATER",1017:"ANGLEPOISE LAMP",1024:"HEATED CABINET",1025:"FRIDGE",1038:"ELECTRIC IRON",1046:"ELECTRIC GRINDER",1057:"MONITOR",1058:"PC",1059:"PRINTER",1060:"TV",1065:"VCR",1066:"AMPLIFIER",1071:"PROJECTOR",1078:"ELECTRIC DRILL",1201:"NETWORK SWITCH",1274:"WORKSHOP POWER TOOLS",1277:"POWER SUPPLY",1278:"RCD BLOCK",1283:"ELECTRO MAGNET",1285:"28 V TRANSFORMER",3007:"UNIVERSAL SERVO CONTROLLER",3008:"GLASSON PSU",3010:"KABUKI DROP",1172:"MIXER",1173:"PROCESSOR",1174:"PLAYBACK",1175:"COMPUTER",1176:"POWERED SPEAKER",1208:"IR SOURCE",3039:"13A > Klik",3040:"Klik > IEC",3041:"PowerCon > 110V",3042:"110V > 13A",3043:"PowerCon > IEC"}
dupesdiviceList ={}
Appliances = {}
testtypes = []
ListTypes = {}
for d in dataout:
    divice = {}
    id  = d['appno']
    divice['user'] = d['user']
    divice['date'] = d['date']
    divice['testnum'] = d['testnum']
    divice['testmode'] = d['testmode']
    try:
        divice['itemtype'] = DiviceTypes[int(d['des1'])]
    except:
        try:
            
            divice['itemtype'] = "Unknown" + d['des1']
        except: 
            divice['itemtype'] = "Unknown"
    divice['location'] = d['loc']
    dpass = True
    try:
        divice['Result'] = {"Visual": d['visual']}
        if(d['visual'] != "P"):
            dpass = False
    except:
        divice['Result'] = {"Visual": "unknown"}
        dpass = False
    
    for t in d['tests']:
        #testtypes.append(t)
        divice['Result'][t] = {}
        if(t in testtypes):
            pass
        else:
            testtypes.append(t)
        #print(t)
        #print("-----")
        if(t in ListTypes):
            pass
        else:
            ListTypes[t] = []

        
        for k in d['tests'][t]:
            divice['Result'][t][k] = d['tests'][t][k]
            if(k == "pass"):
                if(d['tests'][t][k] != "P"):
                    dpass = False

            #print(f"{k}: {d['tests'][t][k]}")
            if(k in ListTypes.get(t, [])):
                pass
            else:
                ListTypes[t].append(k)
    #print(divice)

    #Divice overall result is pass if all tests are pass, otherwise fail. If any test is unknown, then overall result is fail
    if(dpass):
        divice['OverallResult'] = "Pass"
    else:
        divice['OverallResult'] = "Fail"

    #check for duplicate ID, if duplicate, add to dupes list, otherwise add to main list
    if(id in Appliances):
        print("Duplicate ID: " + id + " Adding to dupes list")
        dupesdiviceList[id] = divice
    else:
        Appliances[id] = divice

with open("output.json", "w") as f:    
    json.dump(Appliances, f, indent=4)   



#Asset Tag,Model Name,Next Audit Date,PatTest_Result,Location
output = "Asset Tag,Item Name,Model Name,Next Audit Date,PatTest_Result,Location\n"
for a in Appliances:
    nextdate = (datetime.datetime.strptime(Appliances[a]['date'], "%d-%b-%y") + datetime.timedelta(days=365)).strftime("%Y-%d-%m")
    output += f"{a},{a},{Appliances[a]['itemtype']},{nextdate},{Appliances[a]['OverallResult']},{Appliances[a]['location']}\n"

with open("output.csv", "w") as f:
    f.write(output)

#### Import CSV to SnipeIT



# upload maintenance
from Update import *
update_SnipeIT(Appliances, testtypes)
update_SnipeIT(dupesdiviceList, testtypes)