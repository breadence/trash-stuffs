import pyperclip

allmonths = []

while True:

    inputDataset = input("Write down Month,Days: ")

    if "cancel" in inputDataset:
        break

    inputsplitted = inputDataset.split(",")
    inputmonth = inputsplitted[0]
    inputdays = inputsplitted[1]

    thismonth = (inputmonth, inputdays)
    allmonths.append(thismonth)

everyline = []

for eachset in allmonths:
    themonth = eachset[0]
    thedays = eachset[1]
    
    for i in range(int(thedays)):
        daycounter = i + 1

        if daycounter < 10:
            daystring = "0" + str(daycounter)
        else:
            daystring = str(daycounter)
        
        stringtoadd = f"{themonth} {daystring}"
        everyline.append(stringtoadd)

skiptoday = input("Which day does this month start from?")
skipindex = int(skiptoday) -1

editedeveryline = everyline[skipindex:]
finaleveryline = []

counter = 0
for day in editedeveryline:
    counter += 1
    finaleveryline.append(day)

    if counter == 7:
        counter = 0
        finaleveryline.append("\n")

finalfinalString = ""

for line in finaleveryline:
    print(line)
    finalfinalString += "\n"
    finalfinalString += line

pyperclip.copy(finalfinalString)