import os

import requests
from bs4 import BeautifulSoup as bs
from fileIO import fileIO

def getPageHtmlTree(url):
    page = requests.get(url)
    htmlTree = bs(page.content, features="html.parser")
    return htmlTree 

def getAlphabetResourceList(pageHtmlTree):
    paragraphs = pageHtmlTree.find_all("p")
    for paragraph in paragraphs:
        links = paragraph.find_all("a")
        if len(links) == 26:
            return links 
    return None

def getAlphabetLinkList(baseUrl, alphabetResourceList):
    linkList = []
    for resource in alphabetResourceList:
        link = "{0}{1}".format(baseUrl, resource.get("href"))
        linkList.append(link)
    return linkList

def getAllWordsContent(alphabetLinkList):
    paragraphList = []
    for link in alphabetLinkList:
        pageHtmlTree = getPageHtmlTree(link)
        allParagraphs = pageHtmlTree.find_all("p")
        paragraphList += allParagraphs 
    return paragraphList


baseUrl = "http://www.mso.anu.edu.au/~ralph/OPTED/"
resultsPath = "results"

if __name__ == "__main__":
    basePageHtmlTree = getPageHtmlTree(baseUrl)
    alphabetResourceList = getAlphabetResourceList(basePageHtmlTree)
    alphabetLinkList = getAlphabetLinkList(baseUrl, alphabetResourceList)
    allWordsContent = getAllWordsContent(alphabetLinkList)
    fileIO.writeFile(allWordsContent, resultsPath)

