def readFile(filePath):
    with open(filePath, "r") as f:
        return f.readlines()

def writeFile(allWordsContent, resultsPath):
    with open(resultsPath, "w") as resultsFile:
        for line in allWordsContent:
            lineWithEnding = "{0}\n".format(line)
            resultsFile.write(lineWithEnding)

