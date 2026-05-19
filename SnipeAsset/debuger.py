debuglevel = 3
brokenFile = "broken.csv"
import csv
with open("debug.txt", "w") as f:
    f.write("")
with open("error.txt", "w") as f:
    f.write("")
with open("info.txt", "w") as f:
    f.write("")
def debug(label, data, level = debuglevel):
    if(level == 3):
        print(f"DEBUG - {label}: {data}")
    if(label.lower() == "debug"):
        if(level >= 1):
            with open("debug.txt", "a") as f:
                f.write(f"DEBUG: {data}\n")
    elif(label.lower() == "error"):
        if(level >= 0):
            with open("error.txt", "a") as f:
                f.write(f"ERROR: {data}\n")
    elif(label.lower() == "info"):
        if(level >= 2):
            with open("info.txt", "a") as f:
                f.write(f"INFO: {data}\n")
    else:
        print(f"{label}: {data}")
def logBroken(reason, ID, messgae):
    with open(brokenFile, 'a', newline='') as csvfile:
        fieldnames = ['Type_ID', 'Error']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Broken': reason, 'ID': ID, 'Error': messgae})