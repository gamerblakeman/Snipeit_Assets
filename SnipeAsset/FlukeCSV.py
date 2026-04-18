
from SnipeAsset.debuger import debug
import csv
class FlukeCSV:
    def __init__(self):
        self.broken = []
        self.divices = []

        pass
    def __get_Filedata(self, file):
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            Titles = next(reader)   # ✅ get first row
            data = next(reader)   # ✅ get first row
        return Titles, data
    def save(self, infile):
        if("id" not in self.divice):
            debug("info", f"Appliance without ID found in file {infile}, skipping... Data: {self.divice}")
            self.broken.append({"file": infile, "reason": "Missing ID", "data": self.divice})
        elif(self.divice.get("id", "") == ""):
            debug("info", f"Appliance with empty ID found in file {infile}, skipping... Data: {self.divice}")
            self.broken.append({"file": infile, "reason": "Empty ID", "data": self.divice})
        else:
            debug("info", f"Processing appliance with ID: {self.divice.get('id', 'unknown')}")
            self.divices.append(self.divice)
        
    def getfromFlukeSoftwere(self, infile):
        #{'testnum': '1', 'date': '26-Apr-2026', 'appno': '3443', 'testmode': 'PAT', 'site': 'Site 1', 'site1': 'Location 1', 'site2': 'Location 2', 'user': 'User 1', 'des1': '13A EXTENSION', 'loc': 'Location 1', 'visual': 'P', 'tests': {'Earth Continuity': {'limit': '0.1 ohm', 'measurement': '0.05 ohm', 'result': 'P'}, 'Insulation Resistance': {'limit': '> 1 M ohm', 'measurement': '> 1 M ohm', 'result': 'P'}, ...}}
        self.divices = []
        skip = 31
        
        Titles, data = self.__get_Filedata(infile)
        #location 29th section in the data from lblClientInformation
        self.divice = {}
        file_LOC = data[28]
        self.divice["file"] = infile
        self.divice["location"] = file_LOC
        self.divice["user"] = "unknown"
        self.divice["testnum"] = "0"
        self.divice["testmode"] = "unknown"
        self.divice["Result"] = {}
        stepname = "" 
        skp = 0
        counter = 0
        for index, i in enumerate(Titles):
            if(counter < skip):
                counter += 1
                #continue
            counter += 1
            match i:
                case "txtApplianceNumber": #Reset
                    #stroe the data for the previous appliance before moving on to the next one
                    if(skp == 1):
                        debug("info", f"Skipping appliance with ID: {self.divice.get('ID', 'unknown')} due to previous errors.")
                        skp = 0
                    else:
                        self.save(infile)
                        self.divice = {}
                        self.divice["file"] = infile
                        self.divice["location"] = file_LOC
                        self.divice["user"] = "unknown"
                        self.divice["testnum"] = "0"
                        self.divice["testmode"] = "unknown"
                        self.divice["Result"] = {}

                case "txtApplianceName": #Type ID
                    if(data[index].isnumeric()):
                        self.divice["Type_ID"] = int(data[index])
                    else:
                        self.divice["Type_ID"] = data[index]
                        print("Type ID is not numeric, skipping... " + data[index])
                        skp = 1
                        self.broken.append({"file": infile, "reason": "Type ID is not numeric", "data": data[index]})
                    #self.divice["Type_ID"] = int(data[index])

                case "txtApplianceDate":#2026-04-26
                    month = data[index].split("-")[1]
                    year = data[index].split("-")[0]
                    day = data[index].split("-")[2]
                    if(year == "2026"):
                        year = "2025"
                    self.divice["date"] = year + "-" + month + "-" + day
                    self.divice["nextdate"] = str(int(year) + 1) + "-" + month + "-" + day

                case "txtApplianceInterval":
                    pass
                case "txtApplianceCode": #ID
                    if(data[index].isnumeric()):
                        self.divice["id"] = data[index]
                    else:
                        print("ID is not numeric, skipping... " + data[index])
                        skp = 1
                        debug("info", f"ID is not numeric in file {infile}, skipping appliance with ID: {data[index]}")
                        self.broken.append({"file": infile, "reason": "ID is not numeric", "data": data[index]})
                    if(data[index] == "0"):
                        debug("info", f"Appliance with ID 0 found in file {infile}, skipping...")
                        print("ID is 0, skipping...")
                        skp = 1
                    elif(int(data[index]) <= 0):
                        debug("info", f"ID is not a positive integer in file {infile}, skipping appliance with ID: {data[index]}")
                        self.broken.append({"file": infile, "reason": "ID is not a positive integer", "data": data[index]})
                        skp = 1
                case "txtApplianceResult":
                    self.divice["OverallResult"] = data[index]

                
                case "txtTestStepName":
                    self.divice["Result"][data[index]] = {}
                    #self.divice[data[index]] = {}
                    stepname = data[index]

                case "txtTestStepLimit":
                    self.divice["Result"][stepname]["Limit"] = data[index].replace("\u2265", ">").replace("\u2264", "<")

                case "txtTestStepMeasurement":
                    self.divice["Result"][stepname]["Measurement"] = data[index]

                case "txtTestStepResult":
                    self.divice["Result"][stepname]["Result"] = data[index]

                case _:
                    print("\nUnhandled data point found: " + i + " with value: " + str(data[index]))
                    
        #store the data for the last appliance
        self.save(infile)
        debug("info", f"Finished processing file {infile}, total appliances found: {len(self.divices)}, total broken entries: {len(self.broken)}")
        debug("info", f"Broken entries: {self.broken}")
        debug("info", "_______________________________________________________________________________________________")
        return self.divices
        