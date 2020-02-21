#Inventory.py
#Season Chowdhury
#Lab Section M6
#schowd11
#Lab15
#

def processFile(filename):
    aList = [0,0,0,0]
    inputfile = open(filename, "r")
    for line in inputfile:
        if line.strip() == "hammer":
            aList[0] += 1
        elif line.strip() == "wrench":
            aList[1] += 1
        elif line.strip() == "saw":
            aList[2] += 1
        elif line.strip() == "screw driver":
            aList[3] += 1
    return aList

def fileName(m):
    fileName = m-1
    months = ["January.txt", "February.txt", "March.txt", "April.txt", "May.txt"]
    return months[fileName]

def getValidMonth():
    number = int(input("Enter the month number from 1 - 5: "))
    while not(number <=5 and number>=1):
        number = int(input("Enter the month number from 1 - 5: "))
    return number

def printResults(items,counts):
    for i in range(4):
        print("{0:17}{1}".format(items[i],counts[i]))

def main():
    items = ["hammers","wrenches","saws","screw drivers"]
    number = getValidMonth()
    month = fileName(number)
    printResults(items,processFile(month))
main()


##Output:
##================ RESTART: D:/ECS 102/Labs/Lab 15/Inventory.py ================
##Enter the month number from 1 - 5: 5
##hammers          3
##wrenches         0
##saws             1
##screw drivers    3
##>>> 
##================ RESTART: D:/ECS 102/Labs/Lab 15/Inventory.py ================
##Enter the month number from 1 - 5: 3
##hammers          2
##wrenches         2
##saws             5
##screw drivers    0
##>>> 
##================ RESTART: D:/ECS 102/Labs/Lab 15/Inventory.py ================
##Enter the month number from 1 - 5: 1
##hammers          4
##wrenches         1
##saws             3
##screw drivers    0
##>>> 
##================ RESTART: D:/ECS 102/Labs/Lab 15/Inventory.py ================
##Enter the month number from 1 - 5: 8
##Enter the month number from 1 - 5: 2
##hammers          0
##wrenches         2
##saws             3
##screw drivers    2
##>>> 
