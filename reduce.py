from bs4 import BeautifulSoup as bs
from fileIO import fileIO

def getElementContents(element, contentKey):
    try:
        return element.find(contentKey).contents[0]
    except:
        return ""

def getWordAndType(definition):
    paragraph = bs(definition, features="html.parser")
    word = getElementContents(paragraph, "b")
    wordType = getElementContents(paragraph, "i")
    return word.lower(), wordType

def checkWordLength(word, allowedWordLengths):
    if word is None:
        return False
    return len(word) in allowedWordLengths

def checkWordType(wordType, allowedWordTypes):
    return wordType in allowedWordTypes

def getUniqueList(listWithPotentialduplicates):
    return list(set(listWithPotentialduplicates))

def reduceResults(definitions, allowedWordTypes, allowedWordLengths):
    reducedResults = []
    for definition in definitions:
        word, wordType = getWordAndType(definition)
        if checkWordLength(word, allowedWordLengths) and checkWordType(wordType, allowedWordTypes):
            reducedResults.append(word)
    return getUniqueList(reducedResults)


resultsPath = "results"
reducedResultsPath = "reducedResults"
allowedWordTypes = ["a.", "adj.", "n.", "v. i.", "v. t."]
allowedWordLengths = [4, 5, 6]

if __name__ == "__main__":
    definitions = fileIO.readFile(resultsPath)
    resultsOnlyAllowedWords = reduceResults(definitions, allowedWordTypes, allowedWordLengths)
    fileIO.writeFile(resultsOnlyAllowedWords, reducedResultsPath)
