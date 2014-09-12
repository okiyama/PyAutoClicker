"""
Simple Python Auto-clicker. Soon to use Tkinter for a GUI but at the moment
Command line only. 
Author: Julian Jocque
Date: 7/1/14
"""
from pymouse import PyMouse, PyMouseEvent
import time, random
import pyxhook
from threading import Thread

class AutoClicker(PyMouseEvent):
    def __init__(self, clicksPerSecond = 5, randomizeRange = 0, toggleClick = False, holdClick = True, keyToUse = "Shift_L"):
        PyMouseEvent.__init__(self)
        self.isClicking = False
        if clicksPerSecond > 0:
            self.clicksPerSecond = clicksPerSecond
        else:
            raise ValueError("Clicks per second must be greater than 0.")
        if randomizeRange >= 0:
            self.randomizeRange = randomizeRange
        else:
            raise ValueError("Random range must be greater than or equal to 0.")
        self.mouse = PyMouse()
        self.toggleClick = toggleClick
        self.holdClick = holdClick
        self.keyToUse = keyToUse
        self.initHookManager()

    def initHookManager(self):
        """
        Initializes the HookManager, which the autoclicker uses to get key information globally.
        After this is called, self.hm refers to the HookManaer that was initialized.
        """
        self.hm = pyxhook.HookManager()
        self.hm.HookKeyboard()
        self.hm.KeyDown = self.keyDownHandler
        self.hm.KeyUp = self.keyUpHandler
        self.hm.start()

    def keyDownHandler(self, hookEvent = None):
        """
        Begins the clicking inside of a thread. 
        """
        if hookEvent.Key == self.keyToUse:
            if not self.isClicking:
                Thread(target = self.threadedAutoClick, args=(hookEvent,)).start()
            elif self.toggleClick:
                self.stopClicking()
   
    def threadedAutoClick(self, hookEvent = None):
        """
        Auto clicks inside a thread so that it can be exited by other functions.
        """
        self.isClicking = True
        while(self.isClicking):
            x,y = self.mouse.position()
            self.mouse.click(x,y,1)
            sleepTime = (1.0 / self.clicksPerSecond) #For clicks per second
            if self.randomizeRange != 0.0: #Slight efficiency boost is useful
                sleepTime +=  random.uniform(0.0, (self.randomizeRange / 1000.0)) #For the random delay
            time.sleep(sleepTime)

    def keyUpHandler(self, hookEvent = None):
        """
        Handles any key being released. 
        """
        if hookEvent.Key == self.keyToUse and self.holdClick:
            self.stopClicking()

    def stopClicking(self):
        """
        Stop the clicking
        """
        self.isClicking = False

    def cleanUp(self):
        """
        Cleans up the AutoClicker. 
        You *must* call this when you want to any program which uses this class to end!
        """
        self.hm.cancel()
        self.stopClicking()

def getFloat(message):
    """
    Gets a float from the user by presenting the given message then returns it.
    """
    toRet = -1.0
    while(toRet < 0.0):
        try:
            toRet = float(raw_input(message + " "))
        except ValueError:
            toRet = float(raw_input("Please enter a number greater than 0. "))
    return toRet

def main():
    givenCPS = getFloat("How many clicks per second would you like?")
    givenRandomDelay = getFloat("How much random delay would you like between clicks? \nThis will randomly delay anywhere between 0 and your given number of milliseconds between clicks. 0 is no delay.")
    #TODO Would be nice to ask if they want toggle click or hold click
    #TODO Should also ask what key to use
    clicker = AutoClicker(clicksPerSecond = givenCPS, toggleClick = False, holdClick = True, randomizeRange = givenRandomDelay)
    time.sleep(20)
    clicker.cleanUp()

if __name__ == "__main__":
    main()
