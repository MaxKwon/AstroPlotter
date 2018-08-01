"""
Created on Wed Jul 30 2:10:30 2018
@author: Max K. Kwon 
"""

import Plotter as plot
from tkinter import*



class Runner(Frame):
    
    def __init__(self, master):
        
        Frame.__init__(self, master)
        
        self.master = master 
        
        self.InitializeGUI()
        
        self.plotter = plot.Plotter()
        
    def InitializeGUI(self):
        
        self.master.title("Plotter Controls")
        self.master.geometry("400x300")
        
        self.pack(expand=1)
        
        add_datafile_button = Button(self, text="Select Data", command=self.SelectData) #Button(self, text = "Quit Plotter", command=QuitPlotter)
        add_datafile_button.pack(side=TOP)
        
        plot_all_button = Button(self, text="Plot All", command=self.PlotDataAll)
        plot_all_button.pack(side=LEFT)
        
        plot_none_button = Button(self, text="Blank Plot", command=self.PlotNoData)
        plot_none_button .pack(side=RIGHT)
       
        dropdown_menu = Menu(self.master)
        self.master.config(menu=dropdown_menu)
       
        file = Menu(dropdown_menu)
        file.add_command(label="Quit", command=self.QuitPlotter)
        dropdown_menu.add_cascade(label = "File", menu=file)

    
    def SelectData(self):
        
        return 0
    
    def PlotDataBare(self):
        
        self.plotter.plotFileData()
        print("Plotting Data")
         
        return 0
    
    def PlotDataLimits(self):
        
        self.plotter.plotTelescopeLimit()
        print("Plotting Data Limits")
        
        return 0
    
    def PlotDataCelEq(self):
        
        self.plotter.plotCelEq()
        print("Plotting Cel Eq")
        
        return 0
    
    def PlotDataAll(self):
        
       self.plotter.fullPlot()
       print("Plotting All")
    
    def PlotNoData(self):
        
        self.plotter.plotCelEq()
        self.plotter.plotTelescopeLimit()
        print("Plotting Aux Info")
        
        return 0
    
    def QuitPlotter(self):
        exit()
    
    
root = Tk()

runner = Runner(root)

root.mainloop()
