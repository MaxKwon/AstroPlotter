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
from astroquery.simbad import Simbad
import re #the regular expressions package for detecting input format


filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')
file = open(filename)
data = file.read().splitlines()


#This is hella slow, there is probably a way to do this matrixy? 
#make sure that when this is implemented, that its in a try, should be able to work without internet connection 

ras = []
decs = []

x = True
if (x):
    print(len(data))
    for i in range(len(data)):
 
        print(i)
        result_table = Simbad.query_object(data[i])
        print(len(result_table))
 
        ra = coord.Angle(result_table["RA"][0], unit=u.hour)
        dec = coord.Angle(result_table["DEC"][0], unit=u.degree)
        ra = ra.wrap_at(12 * u.hourangle)
 
        ras.append(ra.radian)
        decs.append(dec.radian)
 
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.scatter(ras, decs)

#ra = coord.Angle('15h17m', unit=u.hour)
#print (ra.radian)
