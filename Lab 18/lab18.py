# lab18.py
# Season Chowdhury
# Lab Section M6
# Have 4 balls move and change color upon click

from graphics import*
from random import randrange

class BBall:
    def __init__(self, color, center, dir=1):
        self.direction = dir
        self.circle = Circle(center,1)
        self.circle.setFill(color)

    def draw(self, win):
        self.win = win
        self.circle.draw(win)

    def move(self, win):
        if self.circle.getCenter().getY() > 8:
            self.direction = -.01
        elif self.circle.getCenter().getY() < -8:
            self.direction = .01

        self.circle.move(0,self.direction)

    def changeColor(self):
        colors=["red","orange","yellow","green","blue","indigo","violet"]
        i = randrange(7)
        self.circle.setFill(colors[i])

        
def main(): 
    win = GraphWin("Bouncing Ball", 700,700)
    win.setCoords(-10,-10,10,10)

    c=Point(0,-9)
    bouncyBall = BBall("red",c)
    bouncyBall.draw(win)

    downBall = BBall("blue",Point(5,9))
    downBall.draw(win)


    midUp = BBall("yellow",Point(-3,0),1)
    midUp.draw(win)


    midDown = BBall("green",Point(-6,0),-1)
    midDown.draw(win)


    while win.checkKey()!='q':
        bouncyBall.move(win)
        downBall.move(win)
        midUp.move(win)
        midDown.move(win)

        if win.checkMouse()!= None:
            bouncyBall.changeColor()
            downBall.changeColor()
            midUp.changeColor()
            midDown.changeColor()
        
    win.close()

main()


