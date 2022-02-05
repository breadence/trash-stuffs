import re

term = r"^(.*?)i(.*?)"
userInput = "i"
theDict = {"hi": "bye", "tee":"hee", "hiii":"danger"}

# print(list(theDict.keys()))

term2 = r"(.*?)"
term3 = "^" + term2 + "i" + term2 + "$"
term4 = f"^{term2}{userInput}{term2}$"
print(term3)
print(term4)

regex = re.compile(term4)



# for each in list(theDict.keys()):

allMatches = list(filter(regex.match, theDict.keys()))

print(allMatches)