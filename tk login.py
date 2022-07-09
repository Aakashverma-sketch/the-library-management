from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import mysql.connector
import os
import sys
w=Tk()
w.geometry('500x300')
#w.resizable(0,0)
user=StringVar()
passwd=StringVar()

def logcheck():
    mydb=mysql.connector.connect(host="localhost", user="root", password="iics", database="project")
    c=mydb.cursor(dictionary=True)
    c.execute("SELECT * FROM login")
    for row in c:
        v1 = row['username']
        v2 = row['password']
        if v1==user.get() and v2==passwd.get():
            messagebox.showinfo("Login", "Login Successfully")
            os.system('Homepage.py')
        else:
            messagebox.showinfo("Login", "Login Denied")

def cancel():
    messagebox.askyesno("Cancel", "Are you sure?")
    sys.exit()

f=Font(family='Lucida console',size=20,weight='bold')
f1=Font(family='Helvetica',size=12,weight='normal')

l1=Label(w,text='LOGIN PORTAL', font=f)
l1.place(x=160, y=20)

l2=Label(w,text='Username', font=f1)
l2.place(x=100, y=100)

l3=Label(w,text='Password', font=f1)
l3.place(x=100, y=150)

e1= Entry(w,textvariable=user)
e1.place(x=210, y=100)

e2= Entry(w,textvariable=passwd, show="*")
e2.place(x=210, y=150)
    
b1=Button(w, text='Submit',command=logcheck, width=10, fg='white', bg='green')
b1.place(x=120, y=200)


b2=Button(w, text='Cancel',command=cancel, width=10, fg='white', bg='red')
b2.place(x=250, y=200)

w.mainloop()
