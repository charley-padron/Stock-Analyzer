from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        #Frame.__init__(self, master)
        Frame.__init__(self, master, background="grey")
        Frame.pack(self)
        self.create_widgets()
        #self.on_button()
        #self.on_button_exit()
        
    def create_widgets(self):
        
        self.label = Label(self, text = "Enter Stocks to search")
        self.label2 = Label(self, text = "Seperate stocks using a comma!")
        self.label.pack()
        self.label2.pack()
        self.entry = Entry(self)
        self.entry.pack()
        
        print(self.entry.get())
        
        self.button1 = Button(self, text = "Search Stocks", command = self.on_button)
        self.button1.pack()
        
        self.button2 = Button(self, text = "Exit", command = self.on_button_exit)
        self.button2.pack()
        
    def on_button(self):
        processInput = self.entry.get()
        print(processInput)
        self.entry.delete(0, 'end')
    
    def on_button_exit(self):
        root.destroy()    
        print("Application ended!")

root = Tk()
root.title("Stock Screener")
#root.Frame("800x500")

app = Application(root)

app.mainloop()