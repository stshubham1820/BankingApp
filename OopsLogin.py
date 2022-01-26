from tkinter import Toplevel
from tkinter import *
import os
from Dashboard import dashboard
#from tryres import Regis
#from OopsMethod import user
class Login:
    def __init__(self) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("LogIn")
        return self.call()
    def details(self):
        self.Name = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()
        self.changes = StringVar()
    def valid(self):
            self.all_user = os.listdir()
            self.name = self.Name.get()
            for i in self.all_user:
                print(i)
                if i == self.name :
                    notify.config(fg="green",text="Your Account Is Here")
                    self.show()
                    return
                else :
                    notify.config(fg="red",text="Register Yourself")
                    #Regis()
    def change(self):
        self.file = open(self.name)
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')
        self.file_data[5] = self.changes
    def forgot(self):
        Label(master = self.screen,text= "Enter New Password ",font=("Calibri",12)).grid(row=7,sticky=W,pady=10)
        Entry(master=self.screen,textvariable=self.changes,font=("Helvetica",12)).grid(row=7,column=0)
        Button(master=self.screen,text="Change Password",command=self.change).grid(row=8,column=0,pady=10)
    
    def Labels(self):
        global notify
        Label(master = self.screen,text= "Login Here : Enter Your User Name & Password ",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
        Label(master = self.screen,text= "Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        notify = Label(master = self.screen,font=("Helvetica",12))
        notify.grid(row=11,sticky=N,pady=10)
    def Enteries(self):
        Entry(master=self.screen,textvariable=self.Name,font=("Helvetica",12)).grid(row=1,column=0)
        Button(master=self.screen,text="Submit",command=self.valid).grid(row=9,column=0,pady=10)
    def show(self):
        Entry(master=self.screen,textvariable=self.Username,font=("Helvetica",12)).grid(row=2,column=0)
        Entry(master=self.screen,textvariable=self.Password,show="*",font=("Helvetica",12)).grid(row=3,column=0)
        Label(master = self.screen,text= "User Name",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
        Label(master = self.screen,text= "Password",font=("Calibri",12)).grid(row=3,sticky=W,pady=10)
        Button(master=self.screen,text="Submit",command=self.final).grid(row=9,column=0,pady=10)
    def final(self):
        self.all_user = os.listdir()
        self.name = self.Name.get()
        self.username = self.Username.get()
        self.password = self.Password.get()
        for i in self.all_user:
            print(i)
            if i == self.name :
                self.check()
                return
            else :
                notify.config(fg="red",text="Register Yourself")
                #Regis()
    def check (self):
        self.file = open(self.name)
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')
        print(self.file_data)
        self.file_pass = self.file_data[5]
        self.file_user = self.file_data[4]
        if self.username == self.file_user :
            if self.password == self.file_pass :
                notify.config(fg="green",text="Login Sucessful")
                dashboard()
            else :
                notify.config(fg="red",text="Wrong Password")
                self.forgot()
        else :
            notify.config(fg="red",text="Wrong User Name")
        return
    def call(self):
        self.details()
        self.Labels()
        self.Enteries()