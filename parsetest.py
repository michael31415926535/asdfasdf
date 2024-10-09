import os
from  datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def main():
    typingSpeed = 10
    outputFileName = ""
    
    logFile = None
    while logFile is None:
        file = str(input("[+] Enter key log file to parse: "))
        if os.path.isfile(file):
            logFile = file
            outputFileName = file + ".txt"
        else:
            print("    [!] Could not find log file!")
    print("[+] Parsing log file...")
    
    rawLines = []
    with open(logFile, "r") as f:
        rawLines = f.readlines()
    
    with open(outputFileName+".txt", "w+") as f:
        lastDateTime = ""
        for line in rawLines:
            if line.strip() == "":
                continue
            currentDateTime = datetime.strptime(line[0:19], DATE_FORMAT)
    
            if lastDateTime == "" or (datetime.strptime(lastDateTime, DATE_FORMAT) + timedelta(seconds=typingSpeed)) < currentDateTime:
                f.write("\n\n"+currentDateTime.strftime(DATE_FORMAT) + ": =+------------------------------------------------------------------------------------------------------+=\n")

            keyPressed = line[len(datetime.now().strftime(DATE_FORMAT)):-1].strip()
            if keyPressed == "Key.enter":
                f.write("\n")
            elif keyPressed == "Key.space":
                f.write(" ")
            elif (len(keyPressed) == 3):
                f.write(keyPressed[1:-1])
            elif keyPressed == "Key.backspace":
                f.write("<-")
            else:
                pass #f.write("["+keyPressed.upper()+"]")

            lastDateTime = line[0:len(datetime.now().strftime(DATE_FORMAT))]

    print("[+] Successfully parsed logs into: " + os.path.join(os.getcwd(), outputFileName+".txt"))
    input("    Press enter to exit...")
        


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()
