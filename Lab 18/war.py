# war.py
# Season Chowdhury
# schowd11
# Lab Section M6
#

from graphics import *
from random import randrange
import math

class Cards:
    def __init__(self, deck):
        self.deck = deck
        
    def shuffle(self):
        for i in range(len(self.deck)-1, -1, -1):
            r = randrange(0,len(self.deck))
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
            
    def dealOut(self, aList, bList):
        for i in range(26):
            aList.append(self.deck[i])
        for k in range(26,52):
            bList.append(self.deck[k])
    
    def display(self):
        print(self.deck)
###########################################   




class Windows:
    def __init__(self,win, img):
        self.win = win
        self.img = img

    def mainMenu(self):
        self.img.draw(self.win)
        welcome = Text(Point(0,12),"Welcome to War")
        greeting = Text(Point(0,3), "Enter your name to Begin the Game")
        welcome.setFill("blue")
        welcome.draw(self.win)
        greeting.setFill("white")
        greeting.draw(self.win)
        nameBox = Entry(Point(0,0), 20)
        nameBox.setText("Name")
        nameBox.setFill("white")
        nameBox.draw(self.win)
        self.nameBox = nameBox
        playButton = Rectangle(Point(-2,-3),Point(2,-1))
        playButton.setFill("green")
        playButton.draw(self.win)
        playButtonText = Text(Point(0,-2), "Play")
        playButtonText.draw(self.win)

    def dealOut(self):
        self.img.draw(self.win)
        computer = Text(Point(-10,18), "Computer")
        computer.setFill("white")
        computer.draw(self.win)
        player = Text(Point(10,-18), self.nameBox)
        Player.setFill("white")
        player.draw(self.win)

#####################################           

def drawWin():
    win = GraphWin("War", 1400, 700)
    win.setCoords(-20,-20,20,20)
    img = Image(Point(0,0),"background.png")
    state = Windows(win, img)
    state.dealOut()
drawWin()


def hide():
    ...
def makeDeck():
    cards = "23456789TJQKA"
    suits = "CDHS"
    deck = []
    for c in cards:
        for s in suits:
            deck.append(c+s)
    return deck

def war(aList, bList, a, b):
    a.append(aList.pop(0))
    a.append(aList.pop(0))
    b.append(bList.pop(0))
    b.append(bList.pop(0))
    print(a)
    print(b)
    result = checkNumber(a[-2],b[-2])
    return result

def checkNumber(a, b):
    cards = "23456789TJQKA"
    for i in cards:
        if a[0] == i:
            numberA = cards.index(i)
        if b[0] == i:
            numberB = cards.index(i)
    if numberA > numberB:
        result = "player1"
    elif numberA == numberB:
        result = "war"
    else:
        result = "player2"
    print(result)    
    return result

def checkResult(aList, bList, a, b, result):
    if result == "player1":
        for i in range(len(b)):
            aList.append(b[i])
            aList.append(a[i])
    elif result == "war":
        result = war(aList, bList, a, b)
        checkResult(aList, bList, a, b, result)
    else:
        for i in range(len(b)):
            bList.append(a[i])
            bList.append(b[i])


def game(aList, bList):
    p = input("press p to put down a card: ")
    while p == "p":
        print(aList)
        print(bList)
        a = []
        b = []
        a.append(aList.pop(0))
        b.append(bList.pop(0))
        print(a[0])
        print(b[0])
        result = checkNumber(a[0],b[0])

        checkResult(aList, bList, a, b, result)
        print(aList)
        print(bList)
        p = input("press p to put down a card: ")
  
def main():
    player1 = []
    player2 = []
    deck = Cards(makeDeck())
    deck.shuffle()
    deck.display()
    deck.dealOut(player1,player2)
    game(player1,player2)


