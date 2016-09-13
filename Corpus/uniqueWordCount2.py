import sys
import os

# To run this program, open a terminal and type "uniqueWordCount.py [foldername]"

# sys.argv is an array containing your command line arguments
root = sys.argv[1] 
#list of names in the folder
fileNames = []
#list of unique words in each file
uniqueWords = []
#total number of unique words
uniqueWordsTotal = 0
#prints the name of the file
print(str(root)+', unique_words')


# This is a for loop that behaves like the java for:each loop. os.listdir
# returns an array of all of the files in a folder.
for f in os.listdir(root):

    # We have to put a slash between the folder name and the filename
    filename = root+"/"+f

    # Open the file with the filename
    infile = file(filename)

    #file = open('filename', 'r') don't actually use

    #creates of string of all characters in file 'filename'
    fileString = infile.read()
    #fileString = fileString.ascii_letters
    # Creates a list of all the words in fileString
    fileList = fileString.split()

    # wordChecked is the word currently being evaluated
    wordChecked = 0
    #checkedAgainst is the word it is being checked against
    checkAgainst = 0
    #Unique count
    uniqueCount = 0


    while wordChecked<len(fileList):
        if fileList.count(fileList[wordChecked]) == 1:
            uniqueCount = uniqueCount + 1
        
        wordChecked = wordChecked + 1
       
    fileNames.append(filename)       
    uniqueWords.append(uniqueCount)
    uniqueWordsTotal = uniqueWordsTotal + uniqueCount

    print(filename + ',' + str(uniqueCount))
    

    # Readlines will take all of the text in the file and give us an array of
    # strings where each string is a line of the file.
    #data = infile.readlines()
    #for l in data:
        #print(l.strip())

    # Close file when you're done with them.
    infile.close()
print("total_unique_words"+str(uniqueWordsTotal))
