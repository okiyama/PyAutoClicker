pyAutoClicker
==================

A very simple Python auto clicker. 
Uses PyMouse to simulate mouse clicks and Tkinter for a GUI.

Very useful for a number of online games.

**Installation**

The only dependencies are on [PyUserInput](https://github.com/SavinaRoja/PyUserInput) and Tkinter. For Ubuntu, this is as simple as 

    sudo apt-get install python-pip python-xlib python-tk  
    sudo pip install PyUserInput

Then you should be all set. You just run autoClickGUI.py to use the program.

***Usage***

At the moment, you use Left Shift to engage the clicking. This will be customizable in the future.  
**Clicks Per Second** is how quickly you want it to click. For web-based games, do not go above 250.  
**MS of Random Delay** places some randomness in the clicks. It will delay a random amount between 0 and the given number of milliseconds between each click. This is useful for avoiding anti-cheat system in online games.  
**Clicking Method** is either Toggle or Hold. With Hold, you hold down the button to keep clicking. With Toggle, you press the button once to start and once to stop.
**Apply Changes** updates the program.


If you are averse to GUIs, there is a much more minimal command line version
if you run autoClicker.py. It is also lacking a few of the options of the GUI.

The only supported platform at the moment is Linux (using X) and Python 2.7.
This could be expanded in the future :)
