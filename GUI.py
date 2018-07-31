"""
Created on Wed Jul 30 2:10:30 2018
@author: Max K. Kwon 
"""

import Plotter as plt
from tkinter import*



class Runner(Frame):
    
    def __init__(self, master):
        
        Frame.__init__(self, master)
        
        self.master = master 
        
        self.InitializeGUI()
    
        self.plotter = plt.Plotter();
        
    def InitializeGUI(self):
        
        self.master.title("GUI")
        self.master.geometry("400x300")
        
        self.pack(expand=1)
        
        add_datafile_button = Button(self, text="Select Data", command=self.SelectData) #Button(self, text = "Quit Plotter", command=QuitPlotter)
        add_datafile_button.pack(side=TOP)
        
        plot_all_button = Button(self, text="Plot All", command=self.PlotDataAll)
        plot_all_button.pack(side=LEFT)
       
        dropdown_menu = Menu(self.master)
        self.master.config(menu=dropdown_menu)
       
        file = Menu(dropdown_menu)
        file.add_command(label="Quit", command=self.QuitPlotter)
        dropdown_menu.add_cascade(label = "File", menu=file)
       
    
    def SelectData(self):
        
        return 0
    
    def PlotDataBare(self):
         
        return 0
    
    def PlotDataLimits(self):
        
        return 0
    
    def PlotDataCelEq(self):
        
        return 0
    
    def PlotDataAll(self):
        
        self.plotter.fullPlot()
    
    def PlotNoData(self):
        
        return 0
    
    def QuitPlotter(self):
        exit()
    
root = Tk()

runner = Runner(root)

root.mainloop()
