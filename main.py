"""
Created on Wed Aug 2 10:51:03 2018
@author: Max K. Kwon 
"""
import Runner as run
from tkinter import *


#Main function for the plotter tool, calls the runner
def main():
  
    root = Tk()
    #Runner object that will call the plotter depending on the user button input 
    runner = run.Runner(root)
    root.mainloop()
  
if __name__== "__main__":
  main()