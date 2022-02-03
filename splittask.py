import pyperclip





ogstring = pyperclip.paste()

splitted = ogstring.split("\n")

week1Tasks = []
week2Tasks = []
week3Tasks = []

for line in splitted:
    bytabs = line.split("\t")

    theTask = bytabs[-1]

    for i in range(0, 3):

        if len(bytabs[i]) == 1:
            weekOfTask = i + 1
            dayOfTask = bytabs[i]

    taskString = str(dayOfTask) + "\t" + theTask

    if weekOfTask == 1:
        week1Tasks.append(taskString)

    elif weekOfTask == 2:
        week2Tasks.append(taskString)

    elif weekOfTask == 3:
        week3Tasks.append(taskString)

grandTotalTasks = []

allWeeksTask = []

allWeeksTask.append(week1Tasks)
allWeeksTask.append(week2Tasks)
allWeeksTask.append(week3Tasks)

for thisWeekTask in allWeeksTask:

    for i in range(1, 8):

        for task in thisWeekTask:
            splittedByTabs = task.split("\t")
            theday = splittedByTabs[0]
            thetask = splittedByTabs[1]

            if int(theday) == i:
                grandTotalTasks.append(task)

        grandTotalTasks.append("")
        
    grandTotalTasks.append("\n-------\n")

returnString = ""

for line in grandTotalTasks:
    returnString += f"{line}\n"

pyperclip.copy(returnString)