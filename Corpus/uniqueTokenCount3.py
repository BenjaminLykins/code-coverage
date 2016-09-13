import sys
import os
from os.path import basename

#Python program that creates a html file with highlighted terms. Currently it prints out one file (the last corpus file analyzed). 
#It also only has two kinds of highlights, which needs to be changed so that it highlights some words greater than others.

#-Terminal command while in folder with the application-  Python uniqueTokenCount2.py targetFolder corpusFolder sequenceLength

# sys.argv is an array containing your command line arguments
targetFile = sys.argv[1]
corpusFile = sys.argv[2]
g = int(sys.argv[3]) #The number of tokens for the sequence of comparison
currentTokens = [] # a list of lists of repeated and unique tokens within the current corpus FILE alone
fullTokensBinary = [] # a list of lists of the total repeated tokens in the corpus FOLDER
fullTokens = [] # a list of the NUMBER of times a sequence has been repeated.
coverage = [] #A list of the percentages of coverage of fullTokens
	
#a function that takes two individual files and compares them and returns a list of the cor file's covered tokens (1's and 0's)
def findSeq(cor, tar):
	targetFileList = tar
	corpusFileList = cor
	#the current sequence of the corpus being evaluated
	corpusSeq = []
	#the sequence of the target program we are evaluating the corpus against
	targetSeq = []
	#the values of how many times a token was repeated in the target file NOT 1's and 0's
	tokens = []
	
	#assigns 0's to all spots in tokens[]
	for a in xrange(0, len(corpusFileList)):
		tokens.append(0)

	#assigns the first sequence of tokens to currentSequence
	for b in xrange(0,g):
		corpusSeq.append(corpusFileList[b])
	
	for c in xrange(0,g):
		targetSeq.append(targetFileList[c])

	for x in xrange(g, len(corpusFileList) + 1): #took away -1 from the len equation
		for y in xrange(g, len(targetFileList) + 1):
			if corpusSeq == targetSeq:
				for t in xrange(0,g):
					tokens[(x-g) + t] +=  1 #changed from =
			if y < (len(targetFileList)):
				targetSeq.append(targetFileList[y])
				targetSeq.pop(0)
		if x < len(corpusFileList):		
			corpusSeq.append(corpusFileList[x])		
			corpusSeq.pop(0)
	return tokens
	
#DEF - takes the list of current tokens and returns one list of just 1's and 0's
def singleListBinary(tok):
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			if tok[x][y] > 0:
				tempTok[y] = 1
	return tempTok
	
def singleList(tok): #takes the list of current tokens and returns the added values of repetitions
	tempTok = [] #tok is a list of the lists of coverage. ex. tok[[0,0,1],[0,1,0],[0,0,0]]
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			tempTok[y] += tok[x][y]
	return tempTok
	

#DEF - takes a list of 1's and 0's and returns the percentage of 1's rounded as an integer
def percentage(tok):
	per = 0
	for x in xrange(0, len(tok)):
		if tok[x] == 1:
			per = per + 1
	per = float(per) / float(len(tok))
	return int(per * 100)
	
def combine(l1, l2): #l1 - corpus Words l2 - Corpus 1's 0's
	l3 = ""
	for x in xrange(0, len(l1)):
		l3 = l3 + " " + l1[x] + "/" + str(l2[x])
	return l3

def greatestIntInList(list): #returns the greatest number in a list. Used to see how many times 255 needs to be divided.
	intToReturn = 0
	for x in xrange(len(list)):
		if(list[x] > intToReturn): #compares all terms
			intToReturn = list[x]
	return intToReturn		
	
def convertToHTML(corpus, coverage): #corpus are the list of words, coverage are if they are covered
	file = open("Test_Html_Doc.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")
	colorDensity = greatestIntInList(coverage)
	
	for x in xrange(0, len(corpus)):
		file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[x] * (255/colorDensity))) + ',' + str(255 - (coverage[x] * (255/colorDensity)))+'")>' + corpus[x] + ' </span>')
	
	file.write("</HEAD>")
	file.write("</BODY>")
	file.close()
	
def convertToHTMLBinary(corpus, coverage): #corpus are the list of words, coverage are if they are covered
	file = open("web_site_test/Test_Html_Doc.html", "w")
	file.write("<HEAD> \n <BODY>")
	file.write("Total Coverage \n")
	
	for x in xrange(0, len(corpus)):
		file.write('<span style = "background-color: rgb(' + '255,' + str(255 - (coverage[x] * (255/3))) + ',' + str(255 - (coverage[x] * (255/3)))+'")>' + corpus[x] + ' </span>')
	
	file.write("</HEAD>")
	file.write("</BODY>")
	file.close()


reps = 0 #used for measuring how many times the loop repeats
for f in os.listdir(corpusFile):
	currentTokens = [] #resets the currentTokens
	# We have to put a slash between the folder name and the filename
	corpus = file(corpusFile+"/"+f).read().split() #a list of all the words in the corpusFile folder, cycling through f.
	
	for d in os.listdir(targetFile):
		target = file(targetFile+"/"+d).read().split() #a list of all the words in the targetFile folder, cycling through d
		currentTokens.append(findSeq(corpus, target))	 	#runs the findSeq definition to find the coverage of a given target file on a given corpus file.
		
	fullTokens.append(singleList(currentTokens)) 		 	#add a single list of the 1's and 0's of the corpus file to the list of final full token coverage
	fullTokensBinary.append(singleListBinary(currentTokens))
	coverage.append(percentage(fullTokens[reps])) 		 	#adds the percentage of coverage of the current corpus file being evaluated to a list of coverage
	#print(basename(corpus) + ' Token Coverage: ' + str(fullTokens[reps])) #prints the list of 1's and 0's of the corpus file being evaluated
	#print(str(percentage(fullTokensBinary[reps])) + '% Coverage') #prints the percentage of the coverage
	print(combine(corpus, fullTokens[reps]))
	convertToHTML(corpus, fullTokens[reps])
	reps = reps + 1										#increases the values of reps. Used for reference only.
