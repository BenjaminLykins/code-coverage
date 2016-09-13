import sys
import os
from os.path import basename

#-In folder with the application-  Python uniqueTokenCount2.py targetFile corpusFile sequenceLength

# sys.argv is an array containing your command line arguments
targetFile = sys.argv[1]
corpusFile = sys.argv[2]
g = int(sys.argv[3]) #The number of tokens for the sequence of comparison
currentTokens = [] # a list of lists of repeated and unique tokens within the current corpus FILE alone
fullTokens = [] # a list of lists of the total repeated tokens in the corpus FOLDER
coverage = [] #A list of the percentages of coverage of fullTokens
	
#a function that takes two individual files and compares them and returns a list of the cor file's covered tokens (1's and 0's)
def findSeq(cor, tar):
	# Open the file with the filename
	targetFile = file(tar)
	#Creates of string of all characters in file 'filename'
	targetFileString = targetFile.read()
	# Creates a list of all the words in fileString
	targetFileList = targetFileString.split()

	#opens the text file, creates a string of the whole file and then breaks it up into a list
	corpusFile = file(cor)
	corpusFileString = corpusFile.read()
	corpusFileList = corpusFileString.split()
	#the current sequence of the corpus being evaluated
	corpusSeq = []
	#the sequence of the target program we are evaluating the corpus against
	targetSeq = []
	#the 1's and 0's saying if the tokens in currentSequence were found in targetSeq
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
					tokens[(x-g) + t] =  1
			if y < (len(targetFileList)):
				targetSeq.append(targetFileList[y])
				targetSeq.pop(0)
		if x < len(corpusFileList):		
			corpusSeq.append(corpusFileList[x])		
			corpusSeq.pop(0)
	return tokens
	
#DEF - takes the list of current tokens and returns one list
def singleList(tok):
	tempTok = []
	for x in xrange(0, len(tok[0])):
		tempTok.append(tok[0][x])
	for x in xrange(1, len(tok)):
		for y in xrange(0, len(tok[x])):
			if tok[x][y] == 1:
				tempTok[y] = 1
	return tempTok

#DEF - takes a list of 1's and 0's and returns the percentage of 1's rounded as an integer
def percentage(tok):
	per = 0
	for x in xrange(0, len(tok)):
		if tok[x] == 1:
			per = per + 1
	per = float(per) / float(len(tok))
	return int(per * 100)
	
reps = 0 #used for measuring how many times the loop repeats
for f in os.listdir(corpusFile):
	# We have to put a slash between the folder name and the filename
	corpus = corpusFile+"/"+f
	currentTokens = []
    
	for d in os.listdir(targetFile):
		target = targetFile+"/"+d
		currentTokens.append(findSeq(corpus, target))	 	#runs the findSeq definition to find the coverage of a given target file on a given corpus file.
	fullTokens.append(singleList(currentTokens)) 		 	#add a single list of the 1's and 0's of the corpus file to the list of final full token coverage
	coverage.append(percentage(fullTokens[reps])) 		 	#adds the percentage of coverage of the current corpus file being evaluated to a list of coverage
	print(basename(corpus) + ' Token Coverage: ' + str(fullTokens[reps])) #prints the list of 1's and 0's of the corpus file being evaluated
	print(str(percentage(fullTokens[reps])) + '% Coverage') #prints the percentage of the coverage
	reps = reps + 1 										#increases the values of reps. Used for reference only.

#print(fullTokens[1])
#print(fullTokens[2])