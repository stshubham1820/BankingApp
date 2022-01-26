from tkinter import Toplevel
from tkinter import *
import os
from OopsLogin import Login
class Register:
    
    def __init__(self) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("Registeration")
        
        return self.call()
    def details(self):
        self.Name = StringVar()
        self.Age = StringVar()
        self.Mobile_Number = StringVar()
        self.Gender = StringVar()
        self.User_name = StringVar()
        self.Password = StringVar()
    def Labels(self):
        global notify
        Label(master = self.screen,text= "Register Here : Enter User Details ",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
        Label(master = self.screen,text= "Full Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        Label(master = self.screen,text= "Age",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
        Label(master = self.screen,text= "Mobile Number",font=("Calibri",12)).grid(row=3,sticky=W,pady=10)
        Label(master = self.screen,text= "Gender",font=("Calibri",12)).grid(row=4,sticky=W,pady=10)
        Label(master = self.screen,text= "User Name",font=("Calibri",12)).grid(row=5,sticky=W,pady=10)
        Label(master = self.screen,text= "Password",font=("Calibri",12)).grid(row=6,sticky=W,pady=10)
        notify = Label(master = self.screen,font=("Helvetica",12))
        notify.grid(row=9,sticky=N,pady=10)    
    def Enteries(self):
        Entry(master=self.screen,textvariable=self.Name,font=("Calibri",12)).grid(row=1,column=0)
        Entry(master=self.screen,textvariable=self.Age,font=("Calibri",12)).grid(row=2,column=0)
        Entry(master=self.screen,textvariable=self.Mobile_Number,font=("Calibri",12)).grid(row=3,column=0)
        Entry(master=self.screen,textvariable=self.Gender,font=("Calibri",12)).grid(row=4,column=0)
        Entry(master=self.screen,textvariable=self.User_name,font=("Calibri",12)).grid(row=5,column=0)
        Entry(master=self.screen,textvariable=self.Password,show="*",font=("Calibri",12)).grid(row=6,column=0)
    def But(self):
        Button(master=self.screen,text="Submit",command=self.final).grid(row=7,column=0,pady=10)
    def final(self) :
        self.name = self.Name.get()
        self.age = self.Age.get()
        self.mobile = self.Mobile_Number.get()
        self.gender = self.Gender.get()
        self.user = self.User_name.get()
        self.password=self.Password.get()
        self.all_user = os.listdir()
        if self.name == "" or self.age == "" or self.mobile == "" or self.gender == "" or self.user == "" or self.password == "" :
            notify.config(fg="red",text="All Fields are Required :",font="Helvetica")
            return
        for i in self.all_user:
            
            if self.name == i :
                print(i)
                notify.config(fg="red",text="Account is Already There",font="Helvetica")
                return
            else :
                new_file = open(self.name,"w")
                new_file.write(self.name+'\n')
                new_file.write(self.age+'\n')
                new_file.write(self.mobile+'\n')
                new_file.write(self.gender+'\n')
                new_file.write(self.user+'\n')
                new_file.write(self.password+'\n')
                new_file.close()
                notify.config(fg="Green",text="Account is being Created",font="Helvetica")
        Login()
    def call(self):
        self.details()
        self.Labels()
        self.Enteries()
        self.But()
      
        