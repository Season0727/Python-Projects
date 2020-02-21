#Recipes.py
#Season Chowdhury
#schowd11
#Lab Section M6
#Lab 15
#

def getRecipe1():
    ingredient = input("Enter the Ingredient: ")
    amount = int(input("Enter the amount: "))
    ask = input("Are there more ingredients? Y/N: ")
    numberOfIng = 1
    while ask.lower() == "y":
        ingredient = input("Enter the Ingredient: ")
        amount1 = int(input("Enter the amount: "))
        ask = input("Are there more ingredients? Y/N: ")
        amount += amount1
        numberOfIng += 1
    return numberOfIng, amount

def getRecipe2():
    print("To stop, press 'enter' for ingredients and enter 0 for amount")
    ingredient = input("Enter the Ingredient: ")
    amount = eval(input("Enter the amount: "))
    numberOfIng = 0
    while ingredient != "":
        ingredient = input("Enter the Ingredient: ")
        amount1 = eval(input("Enter the amount: "))
        amount += amount1
        numberOfIng += 1
    return numberOfIng, amount


def main():
    numberOfIng, amount = getRecipe2()
    print("{0} items equal to {1} grams in total weight".format(numberOfIng,amount))
main()




        
   
##Output with getRecipe1(): 
##================= RESTART: D:\ECS 102\Labs\Lab 15\Recipes.py =================
##Enter the Ingredient: butter
##Enter the amount: 225
##Are there more ingredients? Y/N: y
##Enter the Ingredient: sugar
##Enter the amount: 225
##Are there more ingredients? Y/N: y
##Enter the Ingredient: vanilla extract
##Enter the amount: 4
##Are there more ingredients? Y/N: y
##Enter the Ingredient: egg
##Enter the amount: 44
##Are there more ingredients? Y/N: y
##Enter the Ingredient: baking powder
##Enter the amount: 8
##Are there more ingredients? Y/N: n
##5 items equal to 506 grams in total weight
##>>>

##Output with getRecipe2():
##To stop, press 'enter' for ingredients and enter 0 for amount
##Enter the Ingredient: butter
##Enter the amount: 225
##Enter the Ingredient: sugar
##Enter the amount: 225
##Enter the Ingredient: vanilla extract
##Enter the amount: 4
##Enter the Ingredient: egg
##Enter the amount: 44
##Enter the Ingredient: baking powder
##Enter the amount: 8
##Enter the Ingredient: 
##Enter the amount: 0
##5 items equal to 506 grams in total weight
##>>>  
