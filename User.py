from tkinter import Toplevel
from tkinter import *
import os
from Dashboard import dashboard
#CLASS REGISTER
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
        self.Balance = '0'
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
                new_file.write(self.Balance)
                new_file.close()
                notify.config(fg="Green",text="Account is being Created",font="Helvetica")
        Login()
    def call(self):
        self.details()
        self.Labels()
        self.Enteries()
        self.But()
user = Register
#CLASS LOGIN
class Login:
    def __init__(self) -> None:
        self.screen = Toplevel(master=None)
        self.screen.title("LogIn")
        return self.call()
    def details(self):
        self.Name = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()
        self.changepass = StringVar()
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
            user()#Register Object
    def change(self):
        self.file = open(self.name,"r+")
        self.filedata = self.file.read()
        self.filedata = self.filedata.split("\n")
        self.new = self.file_data[5]
        print(self.new)
        self.file_data[5]=self.changepass.get()
        self.file.seek(0)
        self.file.truncate(0)
        for i in range(len(self.filedata)):
            if i < len(self.filedata)-1 :
                self.file.write(self.filedata[i]+"\n")
            else :
                self.file.write(self.filedata[i])
        print(self.filedata)
        self.file.close()     
    def forgot(self):
        Label(master = self.screen,text= "Enter New Password ",font=("Calibri",12)).grid(row=7,sticky=W,pady=10)
        Entry(master=self.screen,textvariable=self.changepass,font=("Helvetica",12)).grid(row=7,column=0)
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
        self.check()
    def check (self):
        self.file = open(self.name,"r+")
        self.file_data = self.file.read()
        self.file_data = self.file_data.split('\n')
        print(self.file_data)
        self.file_pass = self.file_data[5]
        self.file_user = self.file_data[4]
        if self.username == self.file_user :
            if self.password == self.file_pass :
                notify.config(fg="green",text="Login Sucessful")
                dashboard(self.file_data)
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