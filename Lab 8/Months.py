# Months.txt
# Season Chowdhury
# Lab Section M6
# schowd11@syr.edu
# Print the month name and the number of days based on the number given


def main():
    # set the variable for all the months
    longMonth=["January","February","March","April","May","June","July","August","September","October","November","December"] 
    # Make a list to represent the numbers in each month
    numberOfDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Ask the user for a month
    month = eval(input("Enter a month number: "))
    # Calculate the month number and the number of days 
    monthName, monthDays = longMonth[month-1], numberOfDays[month-1]
    #Print the answer
    print(monthName, "has", monthDays, "days")
main()


# Output

================== RESTART: D:/ECS 102/Labs/Lab 8/Months.py ==================
Enter a month number: 2
February has 28 days
>>> 
================== RESTART: D:/ECS 102/Labs/Lab 8/Months.py ==================
Enter a month number: 4
April has 30 days
>>> 
================== RESTART: D:/ECS 102/Labs/Lab 8/Months.py ==================
Enter a month number: 12
December has 31 days
>>> 
