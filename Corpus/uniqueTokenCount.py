import sys
import os
from os.path import basename

# sys.argv is an array containing your command line arguments
target = sys.argv[1]
corpus = sys.argv[2]
#Total number of unique words
#Prints the name of the file
print(str(target)+', target')
print(str(corpus) + ', corpus')

# Open the file with the filename
targetFile = file(target)
#Creates of string of all characters in file 'filename'
targetFileString = targetFile.read()
# Creates a list of all the words in fileString
targetFileList = targetFileString.split()
#print(targetFileList)

#opens the text file, creates a string of the whole file and then breaks it up into a list
corpusFile = file(corpus)
corpusFileString = corpusFile.read()
corpusFileList = corpusFileString.split()

#length of string to check
g = 5
#the current sequence of the corpus being evaluated
currentSeq = []
#the sequence of the target program we are evaluating the corpus against
targetSeq = []
#the 1's and 0's saying if the tokens in currentSequence were found in targetSeq
tokens = []

#assigns 0's to all spots in tokens[]
for a in xrange(0, len(corpusFileList)):
	tokens.append(0)

#assigns the first sequence of tokens to currentSequence
for b in xrange(0,g):
	currentSeq.append(corpusFileList[b])
	
for c in xrange(0,g):
	targetSeq.append(targetFileList[c])
	
#print(currentSeq)

for x in xrange(g + 1, len(corpusFileList) -1):
	for y in xrange(g + 1, len(targetFileList) -1):
		if currentSeq == targetSeq:
			print('this works')
			#print(currentSeq)
			#print(targetSeq)
			for t in xrange(0,g):
				tokens[y + t] =  1
			#TODO - Assign values of 1 to appropriate tokens.
		targetSeq.append(targetFileList[y])
		targetSeq.pop(0)

	currentSeq.pop(0)
	currentSeq.append(corpusFileList[x])

print(tokens)
	
	
	