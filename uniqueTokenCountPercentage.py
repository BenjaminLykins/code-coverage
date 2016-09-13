import sys
import os
from os.path import basename

#Takes a file for the target and a folder for the corpus and returns the percentage of coverage on the target.

#-Terminal command while in folder with the application-  Python uniqueTokenCount2.py targetFolder corpusFolder sequenceLength


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

#Functions
#findSeq - takes two lists and returns a list of the repeated tokens in sequence length g
#singleListBinary - takes a list of lists and returns a single list with a 1 for every
#	place that a 1 or greater appeared in the lists
#singleList - takes a list of lists and returns a single list with all the values added
#	up for each list
#percentage - takes a list and returns the percentage of tokens that had ones
#combine - combines a list of words and numbers for display purposes
#greatestIntInList - takes a list and returns the greatest number in that list
#convertToHTML - takes a list of coverage and words and writes a file that displays the 
#	coverage with different levels of intensity for more covered words
#convertToHTML Binary - same as the last method only with only one color intensity

# sys.argv is an array containing your command line arguments
targetFile = sys.argv[1] 
corpusFolder = sys.argv[2] 
g = int(sys.argv[3]) 
currentTokens = [] 
fullTokensBinary = [] 
fullTokens = [] 
corpus = []

target = file(targetFile).read().split() #The list of words for the target
targetLength = len(target)
i = 0
for f in os.listdir(corpusFolder):
	corpus.append(file(corpusFolder+"/"+f).read().split()) #a list of all the words in the corpusFile folder, cycling through f.
	i = i + 1

	
#a function that takes two individual files and compares them and returns 
#a list of the target file's covered tokens
#params: list of target' words, list of one of the corpus' files words
#returns: list representing coverage
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
#Param: list of integers
#Returns: list of 1's and 0's
def singleListBinary(tok):
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			if tok[x][y] > 0:
				tempTok[y] = 1
	return tempTok
	
#Takes the list of current tokens and returns the added values of repetitions
#Params: a list of lists representing coverage
#Returns: a single list representing all of the coverage taken from all the comparisons
def singleList(tok): 
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			tempTok[y] += tok[x][y]
	return tempTok

#Takes a list of coverage and returns a percentage based on the amount of coverage
#Params: a list of tokens representing coverage.
#Returns: a percentage of coverage
def percentage(tok):
	per = 0
	for x in xrange(0, len(tok)):
		if tok[x] == 1:
			per = per + 1
	per = float(per) / float(len(tok))
	return str(int(per * 100)) + "% of tokens covered."

#Takes a list of corpus words and coverage and returns them. Used for printing it
#Params: list of words in target, list of coverage
#Returns: String of the words and coverage combined	
def combine(l1, l2): #l1 - corpus Words l2 - Corpus 1's 0's
	l3 = ""
	for x in xrange(0, len(l1)):
		l3 = l3 + " " + l1[x] + "/" + str(l2[x])
	return l3

#Returns the greatest number in a list. Used to see how many times 255 needs to be divided.
#Param: list of numbers
#Returns a single int of the greatest number
def greatestIntInList(list):
	intToReturn = 0
	for x in xrange(len(list)):
		if(list[x] > intToReturn): #compares all terms
			intToReturn = list[x]
	return intToReturn		
	
#Converts a target into a html document with different levels of highlights for more
#repeated tokens
#params: list of words in the target
#		 list of coverage.
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
#params: list of words in the target
#		 list of coverage.
def convertToHTMLBinary(corpus, coverage): #corpus are the list of words, coverage are if they are covered
	file = open("web_site_test/Test_Html_Doc.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")
	
	for x in xrange(0, len(corpus)):
		file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[x] * (255/3))) + ',' + str(255 - (coverage[x] * (255/3)))+'")>' + corpus[x] + ' </span>')
	
	file.write("</HEAD>")
	file.write("</BODY>")
	file.close()

for i in xrange(0,len(corpus)):
	# We have to put a slash between the folder name and the filename	
	currentTokens.append(findSeq(target, corpus[i]))	 	#runs the findSeq definition to find the coverage of a given target file on a given corpus file.
	
fullTokens = singleList(currentTokens) 
fullTokensBinary= singleListBinary(currentTokens)
coverage = percentage(fullTokensBinary)
print(coverage)