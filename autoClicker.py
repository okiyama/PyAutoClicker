"""
Simple Python Auto-clicker. Soon to use Tkinter for a GUI but at the moment
Command line only. 
Author: Julian Jocque
Date: 7/1/14
"""
from pymouse import PyMouse
from pymouse import PyMouseEvent
import time

class AutoClicker(PyMouseEvent):
    def __init__(self, givenDelay = 250, shouldRandomize = False, givenRandomRange = 0):
        PyMouseEvent.__init__(self)
        self.isClicking = False
        self.clickDelay = givenDelay
        self.shouldRandomizeDelay = shouldRandomize
        self.randomizeRange = givenRandomRange
        self.mouse = PyMouse()

    def autoClick(self):
        """
        Does the clicking. Waits the given delay (in ms) between clicks.
        """
        self.isClicking = True
        while(self.isClicking):
            x,y = self.mouse.position()
            print "Clicking at x: ", x , "y: ", y
            self.mouse.click(x,y,1)
            time.sleep(self.clickDelay / 1000.0) #To convert from ms to seconds

    def click(self, x, y, button, press):
        """
        Makes it so we exit on any button click
        """
        print "Just got a button press"
        if press:
            self.isClicking = False

def printOpeningMessage():
    """
    Prints how to use the program
    """
    print "This is a simple autoclicker. To make the clicking stop, press any mouse button.\n"

def getFloat(message):
    """
    Gets a float from the user by presenting the given message then returns it.
    """
    toRet = -1.0
    while(toRet < 0.0):
        try:
            toRet = float(raw_input(message))
        except ValueError:
            toRet = float(raw_input("Please enter a number greater than 0."))
    return toRet

def main():
    printOpeningMessage()
    initialDelay = getFloat("How long would you like the delay before starting the clicking so you can change windows?(in seconds) ")
    mouseDelay = getFloat("How much delay would you like between clicks?(in milliseconds) ")
    clicker = AutoClicker(givenDelay=mouseDelay)
    time.sleep(initialDelay)
    clicker.autoClick()
    clicker.run()

main()
