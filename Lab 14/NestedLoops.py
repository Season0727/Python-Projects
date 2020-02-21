#NestedLoops.py
#Season Chowdhury
#Lab Section M6
#schowd11
#Lab 14 

def partE():
    #Create a nested loop to print the rows without using titles to print on the console
    for row in range(0,80,10):
        for col in range(0,10):
            ans=row+col
            print("{0:<2}".format(ans),end=" ")
        print()
           
def part4():
    #Create a nested loop to print the statements on to the console.
    for num in range(1,8):
        for letter in range(ord("A"),ord("G")):
            output=str(num)+chr(letter)
            print("{0:<1}".format(output), end=" ")
        print()
    #Call the rest of the functions from main to execute them
def main():
    partE()
    part4()
   
main()


##Output:
##=============== RESTART: D:\ECS 102\Labs\Lab 14\NestedLoops.py ===============
##0  1  2  3  4  5  6  7  8  9  
##10 11 12 13 14 15 16 17 18 19 
##20 21 22 23 24 25 26 27 28 29 
##30 31 32 33 34 35 36 37 38 39 
##40 41 42 43 44 45 46 47 48 49 
##50 51 52 53 54 55 56 57 58 59 
##60 61 62 63 64 65 66 67 68 69 
##70 71 72 73 74 75 76 77 78 79 
##1A 1B 1C 1D 1E 1F 
##2A 2B 2C 2D 2E 2F 
##3A 3B 3C 3D 3E 3F 
##4A 4B 4C 4D 4E 4F 
##5A 5B 5C 5D 5E 5F 
##6A 6B 6C 6D 6E 6F 
##7A 7B 7C 7D 7E 7F 
##>>> 
