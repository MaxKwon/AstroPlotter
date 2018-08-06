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
        
        save = 0
        
        T = Text(self.master, height=2, width=30)
        T.pack()
        T.insert(END, "Formats Accepted: TBA")
        
        plot_all_button = Button(self, text="Plot All", command=lambda: self.PlotDataAll(save))
        plot_all_button.grid(row=0, column=0)
        
        plot_data_button = Button(self, text="Plot Data Only", command=lambda: self.PlotDataBare(save))
        plot_data_button.grid(row=1, column=0)
        
        plot_aux_button = Button(self, text="Aux Only Plot", command=lambda: self.PlotNoData(save))
        plot_aux_button.grid(row=2, column=0)
       
        quit_button = Button(self, text="QUIT", command=lambda: self.QuitPlotter(save))
        quit_button.grid(row=4, column=0)
        
        save = IntVar()
        save_check = Checkbutton(self.master, text="Save Graph", variable=save)
        save_check.pack() #will not allow me to try and add it to the same grid as the other buttons for some reason
        #save_check.grid(row=5, column = 0)
        
       # dropdown_menu = Menu(self.master)
       # self.master.config(menu=dropdown_menu)
       
        #file = Menu(dropdown_menu)
        #file.add_command(label="Quit", command=self.QuitPlotter)
        #dropdown_menu.add_cascade(label = "File", menu=file)

    
    def SelectData(self):
        
        return 0
    
    def PlotDataBare(self, save):
        
        self.plotter.plotFileData()
        print("Plotting Data")
        
        if (save.get() == 1):
            self.plotter.savePlot()
         
        return 0
    
    def PlotDataLimits(self, save):
        
        self.plotter.plotTelescopeLimit()
        print("Plotting Data Limits")
        
        if (save.get() == 1):
            self.plotter.savePlot()
        
        return 0
    
    def PlotDataCelEq(self, save):
        
        self.plotter.plotCelEq()
        print("Plotting Cel Eq")
        
        if (save.get() == 1):
            self.plotter.savePlot()
        
        return 0
    
    def PlotDataAll(self, save):
        
       self.plotter.fullPlot()
       print("Plotting All")
       print("save: ", save.get())
       if (save.get() == 1):
            self.plotter.savePlot()
    
    def PlotNoData(self, save):
        
        self.plotter.plotCelEq()
        self.plotter.plotTelescopeLimit()
        print("Plotting Aux Info")
        
        if (save.get() == 1):
            self.plotter.savePlot()
        
        return 0
    
    def QuitPlotter(self):
        sys.exit()
    
    

