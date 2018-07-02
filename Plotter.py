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

class Plotter():
    
    def __init__(self):
        
        self.filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')
        self.fig = plt.figure(figsize=(8,6))
        self.ax = self.fig.add_subplot(111, projection="mollweide")
        
    def detFormat(self, input_str):
        
        regex[1] = '\d{1,2}[h]\d{1,2}[m][+ -]{,1}\d{1,2}[d]\d{1,2}[m]'
        regex[2] = '\d{1,2}[h]\d{1,2}[+ -]{,1}\d{1,2}[d]\d{1,2}'
        regex[3] = '\d{1,3}\s\d{1,3}\s\d{1,3}[.]{,1}\d{,3}\s[+-]{,1}\d{1,3}\s\d{1,3}\s\d{1,3}[.]{,1}\d{,3}' #this will work with rachels now with the addition of '\s' (whitespace in general)
        regex[4] = '\d{1,3}:\d{1,3}:\d{1,3}[.]{,1}\d{,4}[+-]{,1}\d{1,3}:\d{1,3}:\d{1,3}[.]{,1}\d{,4}'
        
        format_index = 0
             
        for i in range(4):
            
            preg = re.compile(regex[i])
            
            if (preg.match(input_str)):
                format_index = i
                break
                    
            
        #FINISH THE OUTPUT, DETERMINE TYPE BASED ON FORMAT_INDEX!!!
        
        #some sort of determination
        #using regex libraries to determine the format of the input for processing 
        
        return form
        
    def getFile(self):
        
        self.filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')
        
    def readFileData(self):
        
        data = ascii.read(self.filename, header_start=0, data_start=0)
        data['ra'].fill_value = "N/A"
        print (data.filled())
        
        
    def plotFileData(self):
        
        data = ascii.read(self.filename, header_start=0, data_start=0)
        data['ra'].fill_value = "N/A"
        
        ra = coord.Angle(data['ra']*u.degree)
        ra = ra.wrap_at(180*u.degree)
        dec = coord.Angle(data['dec']*u.degree)
        
        self.ax.scatter(ra.radian, dec.radian)
        
    def plotCelEq(self):
        
        # To plot the celestial equator in galactic coordinates
        degtorad = math.pi/180.
        alpha = np.arange(-180,180.,1.)
        alpha *= degtorad
        # From Meeus, Astronomical algorithms (with delta = 0)
        x1 = np.sin(192.25*degtorad - alpha)
        x2 = np.cos(192.25*degtorad - alpha)*np.sin(27.4*degtorad)
        yy = np.arctan2(x1, x2)
        longitude = 303*degtorad - yy 
        x3 = np.cos(27.4*degtorad) * np.cos(192.25*degtorad - alpha)
        latitude  = np.arcsin(x3)
        # We put the angles in the right direction
        for i in range(0,len(alpha)):
            if longitude[i] > 2.*math.pi:
                longitude[i] -= 2.*math.pi
            longitude[i] -= math.pi
            latitude[i] = -latitude[i]
        
        # To avoid a line in the middle of the plot (the curve must not loop)
        for i in range(0,len(longitude)-1):
            if (longitude[i] * longitude[i+1] < 0 and longitude[i] > 170*degtorad and longitude[i+1] < -170.*degtorad):
                indice = i
                break
        # The array is put in increasing longitude 
        longitude2 = np.zeros(len(longitude))
        latitude2 = np.zeros(len(latitude))
        longitude2[0:len(longitude)-1-indice] = longitude[indice+1:len(longitude)]
        longitude2[len(longitude)-indice-1:len(longitude)] = longitude[0:indice+1]
        latitude2[0:len(longitude)-1-indice] = latitude[indice+1:len(longitude)]
        latitude2[len(longitude)-indice-1:len(longitude)] = latitude[0:indice+1]
        
        x_plot = []
        y_plot = []
        
        radius = 20
        for i in range(360):
            x = radius * np.cos(i)
            y = radius * np.sin(i)
            
            x_plot.append(x)
            y_plot.append(y)
            
        self.ax.plot(longitude2,latitude2,'g-')
    


plotter = Plotter()
plotter.readFileData()
plotter.plotFileData()
plotter.plotCelEq()







