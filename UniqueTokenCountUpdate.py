#********************************************************************************
# Authors: Benjamin Lykins and Barry Peddycord
# Date: 9/12/2014-11/13/2014
# Version: 3.13
#
# Description: This is a program that will take a target file and compare it to a list
# of files in a corpus folder. Its purpose is to analyze the repetition of code with
# various applications.
#
# To launch the program, navigate to the program location in the terminal window and
# enter the following
# Python uniqueTokenCountUpdate.py *targetFile* *corpusFolder* *sequenceLength*
# The result will print an .html document in the same location as the program.
#********************************************************************************

import sys
import os
from os.path import basename

#Variables
#target - the list of all words in the target
#corpus[] - The list of lists of words in the corpus file
#targetFile - the file passed by the user
#corpusFolder - the folder of corpus files
#g - the length of tokens to be compared
#currentTokens[] - a list that is used to compare to files and then evaluated as a whole
#fullTokensBinary[] - a list of the total repeated tokens on target
#fullTokens[] - a list of the number of times a sequence has been repeated for tokens
#coverage - a percentage of tokens covered
#targetLength - the number of words in the target file

#sys.argv is an array containing your command line arguments
targetFile = sys.argv[1]
corpusFolder = sys.argv[2]
g = int(sys.argv[3])
currentTokens = []
fullTokensBinary = []
fullTokens = []
corpus = []
safehold = 0

targetString = file(targetFile).read().splitlines() #The String of the target used for conversion to html
targetList = []

for x in xrange(0, len(targetString)):
	targetList.append(targetString[x].split())

target = file(targetFile).read().split() #The list of words for the target
targetLength = len(target)
i = 0
for f in os.listdir(corpusFolder):
	corpus.append(file(corpusFolder+"/"+f).read().split()) #a list of all the words in the corpusFile folder, cycling through f.
	i = i + 1


#A function that takes two individual files and compares them and returns a
#list of the the target file's covered tokens.
#Params:    list of target file's words
#			list of the current corpus file's words
#Returns:	list of the coverage.
def findSeq(tar, cor):
	targetFileList = tar
	corpusFileList = cor
	#the current sequence of the corpus being evaluated
	corpusSeq = []
	#the sequence of the target program we are evaluating the corpus against
	targetSeq = []
	#the values of how many times a token was repeated in the target file NOT 1's and 0's
	tokens = []

	#assigns 0's to all spots in tokens[]
	for a in xrange(0, len(targetFileList)):
		tokens.append(0)

	#assigns the first sequence of tokens to currentSequence
	for b in xrange(0,g):
		targetSeq.append(targetFileList[b])

	for c in xrange(0,g):
		corpusSeq.append(corpusFileList[c])

	for x in xrange(g, len(targetFileList) + 1): #took away -1 from the len equation
		for y in xrange(g, len(corpusFileList) + 1):
			if corpusSeq == targetSeq:
				for t in xrange(0,g):
					tokens[(x-g) + t] +=  1
			if y < (len(corpusFileList)):
				corpusSeq.append(corpusFileList[y])
				corpusSeq.pop(0)
		if x < len(targetFileList):
			targetSeq.append(targetFileList[x])
			targetSeq.pop(0)
	return tokens


#Takes the list of current tokens and returns one list of just 1's and 0's
#Params:	List of lists representing coverage
#Returns:	Single list of binary coverage for all of the target/corpus comparisons.
def singleListBinary(tok):
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			if tok[x][y] > 0:
				tempTok[y] = 1
	return tempTok

#Takes the list of lists of current tokens and returns the added values of repetitions
#Params:	A list of coverage
#Returns:	A list representing the total coverage of each token.
def singleList(tok):
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			tempTok[y] += tok[x][y]
	return tempTok

#Takes a list of coverage and returns a percentage based on the amount of coverage
#Params:	A list of tokens representing coverage.
#Returns:	A percentage of coverage (# of ones in list / (#of tokens total)) * 100
def percentage(tok):
	per = 0
	for x in xrange(0, len(tok)):
		if tok[x] == 1:
			per = per + 1
	per = float(per) / float(len(tok))
	return int(per * 100)

#Combines a list of words and numbers. For the purpose of visualization of coverage in
#the terminal window.
#Params:	List of words in the target
#			List representing coverage
#Returns:	String with words and coverage information.
def combine(l1, l2): #l1 - corpus Words l2 - Corpus 1's 0's
	l3 = ""
	for x in xrange(0, len(l1)):
		l3 = l3 + " " + l1[x] + "/" + str(l2[x])
	return l3

#Returns the greatest number in a list. Used to see how many times 255 needs to be divided.
#Params:	List of numbers
#Returns:	Int of the greatest number in the list.
def greatestIntInList(list):
	intToReturn = 0
	for x in xrange(len(list)):
		if(list[x] > intToReturn): #compares all terms
			intToReturn = list[x]
	return intToReturn

#Converts a target into a .html document with different levels of highlights for more
#repeated tokens.
#Params:	List of words in the target
#			List of coverage.
def convertToHTML(corpus, coverage):
	file = open("web_site_test/Test_Html_Doc.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")
	colorDensity = greatestIntInList(coverage)

	for x in xrange(0, len(corpus)):

		file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[x] * (255/colorDensity))) + ',' + str(255 - (coverage[x] * (255/colorDensity)))+'")>' + corpus[x] + ' </span>')

	file.write("</HEAD>")
	file.write("</BODY>")
	file.close()

#Converts a target into an html document with only one level of intensity
#Params:	List of words in the target
#			List of 0's and 1's representing coverage.
def convertToHTMLBinary(corpus, coverage): #corpus are the list of words, coverage are if they are covered
	file = open("web_site_test/Test_Html_Doc.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")

	for x in xrange(0, len(corpus)):
		file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[x] * (255/3))) + ',' + str(255 - (coverage[x] * (255/3)))+'")>' + corpus[x] + ' </span>')

	file.write("</HEAD>")
	file.write("</BODY>")
	file.close()

#Coverts a target into a html document with new lines included.
#Params:	List of words in the target
#			List of coverage.
def convertToHTML2(target, coverage):
	file = open(getFilename(targetFile) + "_Html_Coverage.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")
	colorDensity = greatestIntInList(coverage)
	q = 0

	for x in xrange(0,len(targetList)):
		for y in xrange(0, len(targetList[x])):
			file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[q] * (255/colorDensity))) + ',' + str(255 - (coverage[q] * (255/colorDensity)))+'")>' + target[q] + ' </span>')
			q = q + 1
		file.write('<br>')
	file.close()

#Coverts a target into an html document with new lines and punctuation included.
#Params:	List of words in target
#			List of coverage.



#Takes a filename presumably with a extension and returns the name without the extension.
#Params:	Name of the file
#Returns:	Name of the file without the extension if there is one, and the parameter
#				given if there is not.
def getFilename(name):
	for x in xrange(0,len(name) -1):
		if name[x:x+1] == '.':
			return name[0:x]
	return name

#The actual meat of the code that loops through the files in the corpus folder and gets
#the coverage by comparing them to the corpus. The result is a list of all the comparisons
#which is stored in currentTokens.
#currentTokens is then made into a single list which are used for visualization.
for i in xrange(0,len(corpus)):
	currentTokens.append(findSeq(target, corpus[i]))

fullTokens = singleList(currentTokens)
fullTokensBinary.append(singleListBinary(currentTokens))
coverage = percentage(fullTokens)
#print(combine(target, fullTokens))
#convertToHTML(target, fullTokens)
convertToHTML2(target, fullTokens)
