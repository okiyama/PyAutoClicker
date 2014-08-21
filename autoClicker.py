"""
Simple Python Auto-clicker. Soon to use Tkinter for a GUI but at the moment
Command line only. 
Author: Julian Jocque
Date: 7/1/14
"""
from pymouse import PyMouse, PyMouseEvent
import time
import pyxhook
from threading import Thread

class AutoClicker(PyMouseEvent):
    def __init__(self, givenDelay = 250, shouldRandomize = False, givenRandomRange = 0, toggleClick = False, holdClick = True, keyToUse = "a"):
        PyMouseEvent.__init__(self)
        self.isClicking = False
        self.clickDelay = givenDelay
        self.shouldRandomizeDelay = shouldRandomize
        self.randomizeRange = givenRandomRange
        self.mouse = PyMouse()
        self.toggleClick = toggleClick
        self.holdClick = holdClick
        self.keyToUse = keyToUse

    def autoClick(self, hookEvent = None):
        """
        Does the clicking. Waits the given delay (in ms) between clicks.
        """
        if hookEvent.Key == self.keyToUse and not self.isClicking:
            Thread(target = self.threadedAutoClick, args=(hookEvent,)).start()
   
    def threadedAutoClick(self, hookEvent):
        """
        Auto clicks inside a thread so that it can be exited by other functions.
        """
        self.isClicking = True
        while(self.isClicking):
            x,y = self.mouse.position()
            self.mouse.click(x,y,1)
            time.sleep(self.clickDelay / 1000.0) #To convert from ms to seconds

    def stopClicking(self, hookEvent = None):
        """
        Makes the clicking stop. 
        """
        self.isClicking = False

    def click(self, x, y, button, press):
        """
        Makes it so we exit on any button click
        """
        print("Just got a button press")
        if press:
            self.isClicking = False

def printOpeningMessage():
    """
    Prints how to use the program
    """
    print("This is a simple autoclicker. To make the clicking stop, press any mouse button.\n")

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

def main2():
    mouseDelay = getFloat("How much delay would you like between clicks?(in milliseconds) ")
    clicker = AutoClicker(givenDelay=mouseDelay)
    hm = pyxhook.HookManager()
    hm.HookKeyboard()
    hm.KeyDown = clicker.autoClick
    hm.KeyUp = clicker.stopClicking
    hm.start()
    time.sleep(10)
    hm.cancel()

if __name__ == "__main__":
    #main()
    main2()
