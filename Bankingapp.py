from tkinter import *
import os
from User import Register , Login
screen = Tk()
screen.title("My Bank App")

Label(master = None,text= "My Banking App",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
Label(master = None , text= "Login Page",font=("Calibri",14)).grid(row=1,sticky=N)

Button(master = None , text = "Register",font=("Helvetica",12),command=Register).grid(row=3,sticky=N)
Button(master = None , text = "Login",font=("Helvetica",12),command=Login).grid(row=4,sticky=N,pady=10)
