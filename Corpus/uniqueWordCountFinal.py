import sys
import os
from os.path import basename

# To run this program, open a terminal and type "uniqueWordCountFinal.py [foldername]"

# sys.argv is an array containing your command line arguments
root = sys.argv[1]
#Total number of unique words
uniqueWordsTotal = 0
#Prints the name of the file
print(str(root)+',unique_words')


# This is a for loop that behaves like the java for:each loop. os.listdir
# returns an array of all of the files in a folder.
for f in os.listdir(root):

    # We have to put a slash between the folder name and the filename
    filename = root+"/"+f
    # Open the file with the filename
    infile = file(filename)

    #Creates of string of all characters in file 'filename'
    fileString = infile.read()
    # Creates a list of all the words in fileString
    fileList = fileString.split()

    #The index of the word in fileList currently being evaluated
    wordChecked = 0
    #the unique number of words held in a file
    uniqueCount = 0

    #Repeats for every word in the file
    while wordChecked<len(fileList):
        #Evaluates if the word being checked only appears once
        if fileList.count(fileList[wordChecked]) == 1:
            uniqueCount = uniqueCount + 1
        #Increases the index of the word being checked
        wordChecked = wordChecked + 1

    #Increases the total count of unique words by the number of unique words in the file being evaluated
    uniqueWordsTotal = uniqueWordsTotal + uniqueCount
    #Prints the name of the file and the number of unique words found
    print(basename(filename) + ',' + str(uniqueCount))

    # Close file when you're done with them.
    infile.close()
print("total_unique_words,"+str(uniqueWordsTotal))
