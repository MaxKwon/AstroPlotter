"""
Created on Wed Jul 30 2:10:30 2018
@author: Max K. Kwon 
"""
import Plotter as plot
import threading
import sys
from tkinter import*


class Runner(Frame):
    
    def __init__(self, master):
        
        Frame.__init__(self, master)
        
        self.master = master 
        
        self.InitializeGUI()
        
        self.plotter = plot.Plotter()
        
    def InitializeGUI(self):
        
        self.master.title("Plotter Controls")
        self.master.geometry("300x300")
        
        self.pack(expand=1)
        
        T = Text(self.master, height=2, width=30)
        T.pack()
        T.insert(END, "Formats Accepted: TBA")
        
        plot_all_button = Button(self, text="Plot All", command=self.PlotDataAll)
        plot_all_button.grid(row=0, column=0)
        
        plot_data_button = Button(self, text="Plot Data Only", command=self.PlotDataBare)
        plot_data_button.grid(row=1, column=0)
        
        plot_aux_button = Button(self, text="Aux Only Plot", command=self.PlotNoData)
        plot_aux_button.grid(row=2, column=0)
       
        quit_button = Button(self, text="QUIT", command=self.QuitPlotter)
        quit_button.grid(row=4, column=0)
        
        #save = IntVar()
        #save_check = Checkbutton(self.master, text="Save Graph", variable=save)
        #save_check.grid(row=5, column = 0)
        
       # dropdown_menu = Menu(self.master)
       # self.master.config(menu=dropdown_menu)
       
        #file = Menu(dropdown_menu)
        #file.add_command(label="Quit", command=self.QuitPlotter)
        #dropdown_menu.add_cascade(label = "File", menu=file)

    
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
        sys.exit()
    
    

