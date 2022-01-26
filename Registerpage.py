from tkinter import Toplevel
from tkinter import *
import os
def final():
    name = Name.get()
    age = Age.get()
    mobile = Mobile_Number.get()
    gender = Gender.get()
    user = User_name.get()
    password = Password.get()
    all_user = os.listdir()
    if name == "" or age == "" or mobile == "" or gender == "" or user == "" or password == "" :
        notif.config(fg="red",text="All Fields are Required :")
    else :
        for i in all_user:
            if name == i :
                notif.config(fg="red",text="Account is Already There")
            else :
                new_file = open(name,"w")
                new_file.write(name+'\n')
                new_file.write(age+'\n')
                new_file.write(mobile+'\n')
                new_file.write(gender+'\n')
                new_file.write(user+'\n')
                new_file.write(password)
                new_file.close()
                notif.config(fg="Green",text="Account is being Created")
def Register():
    #MY Variables
    global Name
    global Age
    global Mobile_Number
    global Gender
    global User_name
    global Password
    global notif
    Name = StringVar()
    Age = StringVar()
    Mobile_Number = StringVar()
    Gender = StringVar()
    User_name = StringVar()
    Password = StringVar()
    #Register Screen
    screen = Toplevel(master=None)
    screen.title("Registeration")
    #Register Lable
    Label(master = screen,text= "Register Here : Enter User Details ",font=("Calibri",12)).grid(row=0,sticky=N,pady=10,padx=100)
    Label(master = screen,text= "Full Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
    Label(master = screen,text= "Age",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
    Label(master = screen,text= "Mobile Number",font=("Calibri",12)).grid(row=3,sticky=W,pady=10)
    Label(master = screen,text= "Gender",font=("Calibri",12)).grid(row=4,sticky=W,pady=10)
    Label(master = screen,text= "User Name",font=("Calibri",12)).grid(row=5,sticky=W,pady=10)
    Label(master = screen,text= "Password",font=("Calibri",12)).grid(row=6,sticky=W,pady=10)
    notif = Label(master = screen,font=("Calibri",12))
    notif.grid(row=9,sticky=N,pady=10)
    #Register Entry
    Entry(master=screen,textvariable=Name).grid(row=1,column=0)
    Entry(master=screen,textvariable=Age).grid(row=2,column=0)
    Entry(master=screen,textvariable=Mobile_Number).grid(row=3,column=0)
    Entry(master=screen,textvariable=Gender).grid(row=4,column=0)
    Entry(master=screen,textvariable=User_name).grid(row=5,column=0)
    Entry(master=screen,textvariable=Password,show="@").grid(row=6,column=0)
    #Button
    Button(master=screen,text="Submit",command=final).grid(row=7,column=0,pady=10)
    