#AvgHighLow.py
#Season Chowdhury
#Lab Section M6
#schowd11
#Lab 14


def computerAvg():
    #open the input file and set some variables for future reference
    infile=open("Jan05temps.txt","r")
    count = 0
    sum = 0

   #Create a loop to read the temperatures and also update the previously assigned variables 
    for line in infile:
        temp=int(line)
        count=count+1
        sum=sum + temp
   #Close the file and calulate the average and return the average
    infile.close()
    average=sum/count
    return average


def findHigh():
    #open the input file and set some variables for future reference
    infile=open("Jan05temps.txt","r")
    temp = int(infile.readline())  
    high = temp    

   #Create a loop that checks each current temperature with the previous higest one
    for line in infile:
        temp=int(line)
        if temp>high:
           high = temp

   #Close the file and return the higest temperature
    infile.close()
    return high
    # end of findHigh
   
   
def findLow():
    #open the input file and set some variables for future reference
    infile=open("Jan05temps.txt","r")
    temp = int(infile.readline())  
    low = temp   

    #Create loop to check the current temperature with the previously assigned lowest temperature
    for line in infile:
        temp=int(line)
        if temp<low:
           low = temp  
    #Close the file and return the lowest temperature 
    infile.close()
    return low


def printResults(average,high,low):
    #print results
    print("Average temperature: {0:.2f}".format(average))
    print("High temperature:", high)
    print("Low temperature:", low)


def main():
    #Calls on all of the rest of the functions. Acts like a mother. 
    average=computerAvg()
    high=findHigh()
    low=findLow()
    printResults(average,high,low)  

     
   
main()    
