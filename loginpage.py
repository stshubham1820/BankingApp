from tkinter import Toplevel
from tkinter import *
import os
from typing import Final
def final():
    global all_user
    all_user = os.listdir()
    global name
    global username
    global password
    name = Name.get()
    username = Username.get()
    password = Password.get()
    for i in all_user:
        print(i)
        if i == name :
            notify.config(fg="green",text="Your Account Is Here")
            check()
            return
        else :
            notify.config(fg="red",text="Register Yourself")
def login():
    global Name
    global Username
    global Password
    global notify
    global screen
    Name = StringVar()
    Username = StringVar()
    Password = StringVar()
    #Screen
    screen = Toplevel(master=None)
    screen.title("LogIn")
    #Label
    Label(master = screen,text= "Login Here : Enter Your User Name & Password ",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
    Label(master = screen,text= "Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
    notify = Label(master = screen,font=("Helvetica",12))
    notify.grid(row=9,sticky=N,pady=10)
    #Entry
    Entry(master=screen,textvariable=Name,font=("Helvetica",12)).grid(row=1,column=0)
    Button(master=screen,text="Submit",command=show).grid(row=7,column=0,pady=10)
def show():
    Entry(master=screen,textvariable=Username,font=("Helvetica",12)).grid(row=2,column=0)
    Entry(master=screen,textvariable=Password,font=("Helvetica",12)).grid(row=3,column=0)
    Label(master = screen,text= "User Name",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
    Label(master = screen,text= "Password",font=("Calibri",12)).grid(row=3,sticky=W,pady=10)
    Button(master=screen,text="Submit",command=final).grid(row=7,column=0,pady=10)
def check ():
    file = open(name)
    file_data = file.read()
    file_data = file_data.split('\n')
    print(file_data)
    file_pass = file_data[5]
    file_user = file_data[4]
    if username == file_user :
        if password == file_pass :
            notify.config(fg="green",text="Login Sucessful")
        else :
            notify.config(fg="red",text="Wrong Password")
            
    else :
        notify.config(fg="red",text="Wrong User Name")
    return