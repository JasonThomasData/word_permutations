from fileIO import fileIO

reducedResultsPath = "reducedResults"

summary = { 
    "0": {},
    "1": {},
    "2": {},
    "3": {},
    "4": {},
    "5": {}
}

words = fileIO.readFile(reducedResultsPath)
for word in words:
    for i, char in enumerate(word.lower()):
        if i > 5 or char == "\n":
            continue
        try:
            summary[str(i)][char] += 1
        except KeyError:
            summary[str(i)][char] = 1

for charPlace in summary:
    charPlaceSummary = sorted(summary[charPlace].items(), key=lambda x:x[1], reverse=True)
    print("Results for {0}".format(charPlace))
    for i, charResult in enumerate(charPlaceSummary):
        if i > 3:
            continue
        print(charResult)

        

