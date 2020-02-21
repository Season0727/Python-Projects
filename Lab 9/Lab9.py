# Lab9.py
# Season Chowdhury
# Lab Section M6
# schowd11@syr.edu
# Open file read input and print output in an output file

##def main():
##    # Ask the user for the input file name
##    phrase = input("Enter input file name: ")
##    # Open the given file
##    infile = open(phrase, "r")
##    totalWords = 0
##    wordCount = 0
##    # Run a loop to read each line from the file
##    for line in infile:
##        # Split each line into a list of words
##        words = line.split()
##        # Count the number of characters in each word and the number of words
##        for word in words:
##            wordCount += len(word)
##            totalWords += 1
##        # Calculate the avg number of characters per word in each line
##        avgWordLen = wordCount / totalWords
##        # Print the avg word length of each line
##        print(line, avgWordLen)
##        wordCount = 0
##        totalWords = 0
##    # Closes the file
##    infile.close()
##main()


def main():
    # Ask the user for the input file name
    inFileName = input("Enter input file name: ")
    outFileName = input("Enter output file name: ")
    # Input file
    infile = open(inFileName, "r")
    # Output file
    outfile = open(outFileName, "w")
    lineList = infile.readlines()
    totalWords = 0
    wordCount = 0
    # Run a loop to read each line from the file
    for line in lineList:
        # Split each line into a list of words
        words = line.split()
        # Count the number of characters in each word and the number of words
        for word in words:
            wordCount += len(word)
            totalWords += 1
        # Calculate the avg number of characters per word in each line
        avgWordLen = wordCount / totalWords
        # Print the avg word length of each line
        print(line, avgWordLen, file=outfile)
        wordCount = 0
        totalWords = 0
    # Closes the files
    infile.close()
    outfile.close()
main()




####Output to screen:
##Enter input file name: Seasons.txt
##Enter output file name: Seasonstats.txt
##>>>


##Output to file:
##Thirty days hath September
## 5.75
##April, June, and November
## 5.5
##All the rest have thirty-one
## 4.8
##Except February, which has twenty-eight.
## 7.2

