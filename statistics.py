from fileIO import fileIO

characters = [
    ["s","c","p","b"],
    ["a","o","e","i"],
    ["r","a","n","l"],
    ["e","i","a","t"],
    ["e","a","l",""],
    ["e","r","y",""]
]


reducedResultsPath = "reducedResults"
reducedListOfDefinitions = fileIO.readFile(reducedResultsPath)
wordsCount = 0

for char_0 in characters[0]:
    for char_1 in characters[1]:
        for char_2 in characters[2]:
            for char_3 in characters[3]:
                for char_4 in characters[4]:
                    for char_5 in characters[5]:
                        word = "{0}{1}{2}{3}{4}{5}".format(char_0, char_1, char_2, char_3, char_4,
                                char_5)
                        if "{0}\n".format(word) in reducedListOfDefinitions:
                            wordsCount += 1
                            print(word)

print("Results produce {0} valid words".format(wordsCount))
