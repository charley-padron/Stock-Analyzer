#Used for GUI
from tkinter import *

#Used for plotting the stock data
import matplotlib as plt

#Used to access stock data
import alpha_vantage

#alpha_vantage key
#is private to indivduals 
#and required to access alpha_vantage

#Used to get the stock data in JSON format 
import requests

#Used to store stock data
#And perform calculations for MACD and RSI
import numpy as np 

class Application(Frame):
    
    def __init__(self, master):
        #Frame.__init__(self, master)
        Frame.__init__(self, master, background="grey")
        Frame.pack(self, fill="both", expand=True)
        self.create_widgets()
        #self.on_button()
        #self.on_button_exit()
        
    def create_widgets(self):
        
        self.label = Label(self, text = "Enter Stocks to search")
        self.label2 = Label(self, text = "Seperate stocks using a comma and no spaces.")
        self.label.pack()
        self.label2.pack()
        self.entry = Entry(self)
        self.entry.pack()
        
        print(self.entry.get())
        
        self.button1 = Button(self, text = "Search Stocks", command = self.on_button)
        self.button1.place(x=340,y=65)
        
        self.button2 = Button(self, text = "Exit", command = self.on_button_exit)
        self.button2.place(x=440, y=65)
        
    def on_button(self):
        processInput = self.entry.get()
        print(processInput)
        self.entry.delete(0, 'end')
        
        #process the string and continue with project
        self.stock(processInput)
    
    def on_button_exit(self):
        root.destroy()    
        print("Application ended!")
    
    def stock(self, stocks):
        print(stocks + " new")
        stocks = stocks.split(',')
        for stock in stocks:
           print(stock)
           
        #matplotlib in  tkinter
        #try each symbol, if symbol not found 
        #return error and continue through list

root = Tk()
root.title("Stock Screener")
root.geometry("800x500")

app = Application(root)

app.mainloop()