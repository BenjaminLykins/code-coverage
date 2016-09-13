import unittest
import sys
import os
from os.path import basename

# These Tests check the main functionality of uniqueTokenCount. 


#a function that takes two individual files and compares them and returns a list of the cor file's covered tokens (1's and 0's)
def findSeq(cor, tar, length):

	corpusFileList = cor
	targetFileList = tar
	g = length
	
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


#***************************************************************************************************************

class runTests(unittest.TestCase):

	
	def singleList(self):
		l1 = [0,0,0,0,1]
		l2 = [1,0,0,0,0]
		l3 = [l1,l2]
		l4 = singleList(l3)
		self.assertEqual(l4, [1,0,0,0,1]) #Tests that singleList can take two lists and return the correct combined list
	
	def testPercentage(self):
		l1 = [0,1]
		per = percentage(l1)
		self.assertEqual(50, per)
	
	def testCoverage(self):
		corpus = [0,0,0,3,3,0,0]
		target = [1,1,3,3,1,1,1,1,1,1,1]
		coverage = findSeq(corpus, target, 2)
		self.assertEqual(coverage, [0,0,0,1,1,0,0]) #Normal Test
		
		corpus = [3,3,0,0,0,0,3,3]
		target = [3,3]
		coverage = findSeq(corpus,target,2)
		self.assertEqual(coverage, [1,1,0,0,0,0,1,1]) #edges
		
		corpus = [1,1,1,1,1,1,1]
		target = [4,4,4,4,4,4,4,4,4,4,4,4]
		coverage = findSeq(corpus, target, 1)
		self.assertEqual(coverage, [0,0,0,0,0,0,0]) #no repeats
		
		
	
if __name__ == '__main__':
    unittest.main()

		
		