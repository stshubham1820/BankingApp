import os
from tkinter import *
class Edit:
    def call(self):
        self.file = open(self.name,"r+")
        self.file_data = self.file.read()
        self.file_data = self.file_data.split("\n")
        Label(master = self.screen,text="Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        Entry(master=self.screen,textvariable=self.new_Name,font=("Calibri",12)).grid(row=1,column=0,padx=10)

    def __init__(self,Name) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("Edit Account")
        self.name = Name
        self.new_Name = StringVar()
        return self.call()

class Help:
    def __init__(self) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("Helpline")
        Label(master = self.screen,text="Mobile Number",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        Label(master = self.screen,text="+91 8319809996",font=("Calibri",12)).grid(row=1,column=0,sticky=N,pady=10)
        Label(master = self.screen,text="Mail",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
        Label(master = self.screen,text="contact.newerafoundation@gmail.com",font=("Calibri",12)).grid(row=2,column=0,sticky=N,pady=10)
        Label(master = self.screen,text="Website",font=("Calibri",12)).grid(row=3,sticky=W,pady=10)
        Label(master = self.screen,text="http://www.thenewerafoundation.in/",font=("Calibri",12)).grid(row=3,column=0,sticky=N,pady=10)
        Label(master = self.screen,text="All Rights are Reserved with The New Era Foundation",font=("Calibri",12)).grid(row=3,sticky=N,pady=10)