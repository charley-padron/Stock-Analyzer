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

#USed to print JSON stock data
import json

#Used to print clean version of JSON
import pprint

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
           #retrive stock data
           self.retrieve(stock)
           self.graph(stock)
           
        #matplotlib in  tkinter
        #try each symbol, if symbol not found 
        #return error and continue through list
    
    def retrieve(self, stock):
        
        #Stock Data website
        URL = "https://www.alphavantage.co/query"
        
        function = "TIME_SERIES_DAILY"
        symbol = stock
        #private key
        api_key = ""
        
        #Specifics for data retrieval
        #Retieves data for the past 100 days
        param = { "function" : function, "symbol" : symbol, "apikey" : api_key}
        
        #Holds JSON format of stock data
        data = requests.get(URL, params = param)
        
        pprint.pprint(data.json())
        
        #make new function named graph that gets called in stock
        #graph calls retreive and graphs the stock in matplotlib and formats it as a ne    
        #window for each stock
       
       # Funciton to graph the stocks data and implement it as a window for each stock 
    def graph(self, stock):
        print("Graphing data for: " + stock)

root = Tk()
root.title("Stock Screener")
root.geometry("800x500")

app = Application(root)

app.mainloop()