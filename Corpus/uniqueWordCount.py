import sys
import os

# To run this program, open a terminal and type "uniqueWordCount.py [foldername]"

# sys.argv is an array containing your command line arguments
root = sys.argv[1] 
fileNames = [] #list of names in the folder
uniqueWords = [] #list of unique words in each file
uniqueWordsTotal = 0 #total number of unique words


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
    #false while loop repeats, true if repeat word is found
    breakLoop = 0
    #Unique count
    uniqueCount = 0

    # A String assigned to the current word that we will be checking
    currentWord = 0

    while wordChecked<len(fileList):
 #      currentWord = fileList[i]
        while breakLoop == 0:
            while checkAgainst<len(fileList):
                if fileList[wordChecked] == fileList[checkAgainst]:#if the word is repeated
                    if wordChecked != checkAgainst: #not including the word being checked
                        breakLoop = 1 
                checkAgainst = checkAgainst + 1 
            if breakLoop == 0: #if the loop was never broken because of a repeated word
                uniqueCount =  uniqueCount + 1
                breakLoop = 1
                print("here")
    
        wordChecked = wordChecked + 1
        checkedAgainst = 0
            
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
print(uniqueWordsTotal)
