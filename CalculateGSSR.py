""" year
    name
    print ratings
    write rating

in the end, calculate all ratings

ratings:
    WANT
    fine
    don't want
    dupe


wholeDict = {}

while True:

    theName = input("Name: ")
    theRating = input("Rating: ")

    if (theName == "q") or (theRating == "q"):
        break
    else:
        wholeDict[theName] = {"rating": theRating}

rated1 = []
rated2 = []
rated3 = []
rated4 = []

for servant in wholeDict:
    servantRating = wholeDict[servant]["rating"]

    if servantRating == "1":
        rated1.append(servant)
    elif servantRating == "2":
        rated2.append(servant)
    elif servantRating == "3":
        rated3.append(servant)
    elif servantRating == "4":
        rated4.append(servant)

servantLength = len(wholeDict) """

import pyperclip


servants = (pyperclip.paste()).split("\r\n")




def swapList(theList):
    toReturn = []

    for each in theList:
        splitted = each.partition(" ")
        space1 = splitted[0]
        space2 = splitted[2]

        newString = space2 + " " + space1

        toReturn.append(newString)

    return toReturn


swappedThing = swapList(servants)

swappedThing.sort(reverse=True)

theFinal = swapList(swappedThing)


toCopy = "\n".join(theFinal)

pyperclip.copy(toCopy)