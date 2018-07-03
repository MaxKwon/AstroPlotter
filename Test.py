"""
Created on Wed Jun 26 10:51:03 2018
@author: Max K. Kwon 
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import fits
from tkinter.filedialog import askopenfilename
from tkinter import *
import math
import re #the regular expressions package for detecting input format

        
filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')

with open(filename) as f:
    content = f.readlines()
    
print (content[1])