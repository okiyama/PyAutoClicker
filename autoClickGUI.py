"""
GUI for a Linux auto-clicker written in python. 
Uses Tkinter to get relevant info from the user to create an AutoClicker object.

Author: Julian Jocque
Date: 8/16/14
"""

from autoClicker import AutoClicker
import Tkinter as tk

class AutoClickerGUI:
    def test(self):
        window = tk.Tk()
        window.mainloop()

if __name__ == "__main__":
    gui = AutoClickerGUI().test()
