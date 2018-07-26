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
import astroquery.simbad #using to fill blank data points with queries from simbad database
import re #the regular expressions package for detecting input format

class Plotter():
    
    def __init__(self):
        
        self.test = False
        
        self.filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')
        self.fig = plt.figure(figsize=(8,6))
        self.ax = self.fig.add_subplot(111, projection="mollweide")
        
        self.form = self.detFormat()
        print(self.form)
        
    def detFormat(self): #BROKEN
        
        with open(self.filename) as f:
            content = f.readlines()
    
        if (self.test):
            print (content[1]) # first actual row of the data content[0] is the headers
              
        regex = []
        regex.append('\d{1,2}[h]\d{1,2}[m]\s[+ -]{,1}\d{1,2}[d]\d{1,2}[m]') #15h17m -11d10m
        regex.append('\d{1,2}[h]\d{1,2}\s[+ -]{,1}\d{1,2}[d]\d{1,2}') #15h17 +89d15
        regex.append('\d*\s*\d*[.]{,1}\d*\s*\d{1,3}\s\d{1,3}\s\d{1,3}[.]{,1}\d{,3}\s[+-]{,1}\d{1,3}\s\d{1,3}\s\d{1,3}[.]{,1}\d{,3}') #20 54 05.689 +37 01 17.38 
        regex.append('\d{1,3}:\d{1,3}:\d{1,3}[.]{,1}\d{,4}\s[+-]{,1}\d{1,3}:\d{1,3}:\d{1,3}[.]{,1}\d{,4}') # 10:12:45.3 -45:17:50
          
        format_index = 9
             
        for i in range(4): 
            preg = re.compile(regex[i]) 
            if (preg.match(content[1])):
                format_index = i
                break
        
        form = "N/A"
        
        if (format_index == 0):
            form = "a"
        elif (format_index == 1):
            form = "b"
        elif (format_index == 2):
            form = "c"
        elif (format_index == 3):
            form = "d"
        
        return form
    
    def formatData(self, form):
        
        data = ascii.read(self.filename)
        
        ras = []
        decs = []
        
        #Have all the formats be ID, REC, DEC and let it be the users problem after that 
        
        if (form == "a" or form == "b" or form == "d"):
            for i in range(len(data)):
                ra_str = str(data[i][1])
                dec_str = str(data[i][2])
                
                ra = coord.Angle(ra_str, unit=u.hour)
                dec = coord.Angle(dec_str, unit=u.degree)
                ra = ra.wrap_at(12 * u.hourangle)
 
                ras.append(ra.radian)
                decs.append(dec.radian)
        
        elif (form == "c"): 
            for i in range(len(data)):
                ra_str = str(data[i][2]) + ":" + str(data[i][3]) + ":" + str(data[i][4]) #should start at data[i][1] but the test data has another garbage data column
                dec_str = str(data[i][5]) + ":" + str(data[i][6]) + ":" + str(data[i][7])
                
                ra = coord.Angle(ra_str, unit=u.hour)
                dec = coord.Angle(dec_str, unit=u.degree)
                ra = ra.wrap_at(12 * u.hourangle)
 
                ras.append(ra.radian)
                decs.append(dec.radian)
        
        return ras, decs
        
    def getFile(self):
        
        self.filename = askopenfilename(filetypes=[("Text Files", "*.txt")], title='Data')
        
    def printFileData(self): #BROKEN
        
        #Maybe take this stuff out i dont know, need it to know delimination or something I guess
        if (self.form == "c"):
            del_ = "\s"
            d_s = 1
        elif (self.form == "a" or self.form == "b"):
            del_ = "\s"
            d_s = 0
            
        
        data = ascii.read(self.filename, delimiter = del_, data_start=d_s)
        print (data)
        print (type(data))
            
        
    def plotFileData(self): 
    
        ras, decs = self.formatData(self.form)
        
        self.ax.scatter(ras, decs)
        
        
        
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
        
    def plotTelescopeLimit(self):
        
        #limits for the gemini north telescope 
        dec_lim = [-30, 73] #degrees
        ra_lim = [105, 345] #degrees
        
        ra = coord.Angle(ra_lim*u.degree)
        ra = ra.wrap_at(180*u.degree)
        dec = coord.Angle(dec_lim*u.degree)
        
        #maybe clean this up 
        self.ax.plot([ra[0].radian, ra[0].radian], [dec[0].radian, dec[1].radian], "k-")
        self.ax.plot([ra[0].radian, ra[1].radian], [dec[1].radian, dec[1].radian], "k-")
        self.ax.plot([ra[1].radian, ra[1].radian], [dec[1].radian, dec[0].radian], "k-")
        self.ax.plot([ra[1].radian, ra[0].radian], [dec[0].radian, dec[0].radian], "k-")
        
    def fullPlot(self):
        
        self.plotCelEq()
        self.plotTelescopeLimit()
        self.plotFileData()
        
        
    
plotter = Plotter()
#plotter.plotTelescopeLimit()
#plotter.plotCelEq()
#plotter.printFileData()
plotter.fullPlot()






