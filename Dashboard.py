from tkinter import Toplevel
from tkinter import *
import os
from Accout import Edit , Help
class dashboard:
    def __init__(self,Data) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("Dashboard")
        self.data = Data
        return self.call()
    def Labels(self):
        global notify
        Label(master = self.screen,text= "User Dashboard : Here You can perform certain Task ",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
        Label(master = self.screen,text= "Account Details",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        Label(master = self.screen,text= "Deposite",font=("Calibri",12)).grid(row=8,sticky=W,pady=10)
        Label(master = self.screen,text= "Withdraw",font=("Calibri",12)).grid(row=10,sticky=W,pady=10)
        Label(master = self.screen,text= "Edit Profile",font=("Calibri",12)).grid(row=12,sticky=W,pady=10)
        Label(master = self.screen,text= "Help Center",font=("Calibri",12)).grid(row=13,sticky=W,pady=10)
        Label(master = self.screen,text= "Feedback",font=("Calibri",12)).grid(row=14,sticky=W,pady=10)
    def profile(self):
        List = ["Name"," Age","Mobile Number","Gender","User Name","Password"]
        for i in range(len(self.data)-1):
            Label(master = self.screen,text= self.data[i],font=("Calibri",12)).grid(row=i+2,sticky=N,pady=10)
            Label(master = self.screen,text= List[i],font=("Calibri",12)).grid(row=i+2,sticky=W,pady=10)
        #Label(master = self.screen,text=final.name,font=("Helvetica",12)).grid(row=8,sticky=N,pady=10,padx=100)
    def Edit(self):
        Edit(self.data[0])
    def Depo(self):
        #global take
        self.amo = StringVar()
        def add():
            amo = self.amo.get()
            if amo == "" or float(amo) == 0 or float(amo) < 0:
                notif.config(fg="red",text="Unsucessful")
                return
            else :

                self.file = open(self.data[0],"r+")
                self.filedata = self.file.read()
                self.filedata = self.filedata.split("\n")
                Current_Balance = self.filedata[6]
                Update_Balance = float(Current_Balance)
                Update_Balance = Update_Balance + float(amo)
                self.filedata[6]=  str(Update_Balance)
                self.file.seek(0)
                self.file.truncate(0)
                for i in range(len(self.filedata)):
                    if i < len(self.filedata)-1 :
                        self.file.write(self.filedata[i]+"\n")
                    else :
                        self.file.write(self.filedata[i])
                Label(master = self.screen,text= "Current Balance : "+self.filedata[6],font=("Calibri",12)).grid(row=9,column=0,sticky=W,pady=10)
                print(self.filedata)
                self.data[6] = self.filedata[6]
                self.file.close()
                
                notif.config(fg="red",text="Sucessful")
                return
        Label(master = self.screen,text= "Current Balance : "+self.data[6],font=("Calibri",12)).grid(row=9,column=0,sticky=W,pady=10)
        Label(master = self.screen,text= "Amount",font=("Calibri",12)).grid(row=9,column=1,sticky=W,pady=10)
        Entry(master=self.screen,textvariable=self.amo,font=("Calibri",12)).grid(row=9,column=2,padx=10)
        notif = Label(master=self.screen,font=("Calibri",12))
        notif.grid(row=9,column=4,pady=10,padx=20)
        Button(master=self.screen,text="Credit",command=add).grid(row=9,column=3,pady=10)
        
    def With(self):
        self.cut = StringVar()
        def sub():
            amo = self.cut.get()
            if amo == "" or float(amo) == 0 or float(amo) < 0:
                notif.config(fg="red",text="Unsucessful")
                return
            else :

                self.file = open(self.data[0],"r+")
                self.filedata = self.file.read()
                self.filedata = self.filedata.split("\n")
                Current_Balance = self.filedata[6]
                Update_Balance = float(Current_Balance)
                Update_Balance = Update_Balance - float(amo)
                self.filedata[6]=  str(Update_Balance)
                self.file.seek(0)
                self.file.truncate(0)
                for i in range(len(self.filedata)):
                    if i < len(self.filedata)-1 :
                        self.file.write(self.filedata[i]+"\n")
                    else :
                        self.file.write(self.filedata[i])
                Label(master = self.screen,text= "Current Balance : "+self.filedata[6],font=("Calibri",12)).grid(row=11,column=0,sticky=W,pady=10)
                print(self.filedata)
                self.data[6] = self.filedata[6]
                self.file.close()
                
                notif.config(fg="red",text="Sucessful")
                return
        Label(master = self.screen,text= "Current Balance : "+self.data[6],font=("Calibri",12)).grid(row=11,column=0,sticky=W,pady=10)
        Label(master = self.screen,text= "Amount",font=("Calibri",12)).grid(row=11,column=1,sticky=W,pady=10)
        Entry(master=self.screen,textvariable=self.cut,font=("Calibri",12)).grid(row=11,column=2,padx=10)
        notif = Label(master=self.screen,font=("Calibri",12))
        notif.grid(row=11,column=4,pady=10,padx=20)
        Button(master=self.screen,text="Debit",command=sub).grid(row=11,column=3,pady=10)
    def Buttons(self):
        Button(master=self.screen,text="Profile",command=self.profile).grid(row=1,column=0,pady=10)
        Button(master=self.screen,text="Deposite",command=self.Depo).grid(row=8,column=0,pady=10)
        Button(master=self.screen,text="Withdraw",command=self.With).grid(row=10,column=0,pady=10)
        Button(master=self.screen,text="Edit",command=self.Edit).grid(row=12,column=0,pady=10)
        Button(master=self.screen,text="Help Center",command=Help).grid(row=13,column=0,pady=10)
        Button(master=self.screen,text="Feedback").grid(row=14,column=0,pady=10)
    def call(self):
        self.Labels()
        self.Buttons()