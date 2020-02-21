# read numbers from a file into a list
# Season Chowdhury
# numbers are ints
# fileName is the name of the file
# returns the list
def readNumbers(fileName):
    numfile=open(fileName,"r")
    numList=[]
    for line in numfile:
        numList.append(int(line))
    numfile.close()

    return numList

def average(aList):
    sum = 0
    count = 0
    for i in aList:
        sum += i
        count +=1
    average = sum/count
    return average

def stdDev(aList, avg):
  sum = 0
  for i in range(len(aList)):
    sum += ((avg - aList[i])**2)
  return ((sum / len(aList))**.5)

def copy(aList):
    bList =[]
    for i in aList:
        bList.append(i)
    return bList

def median(bList):
    bList.sort()
    if (len(bList)%2)==0:
         n = int((len(bList)/2))
         median = (bList[n]+ (bList[n-1]))/2
    else:
        n = int((len(bList)-1)/2)
        median = bList[n]

    return median



def main():
    numList = readNumbers("ages.txt.")
    avg = average(numList)
    stdDeviation = stdDev(numList, avg)
    newList = copy(numList)
    medianOfCopy = median(newList)
    print(numList)
    print(avg)
    print("{0:.2f}".format(stdDev(newList,avg)))
    print(newList)
    print(median(newList))
    
main()    
