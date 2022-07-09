from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from addBooks import *
from deleteBooks import *
from viewBooks import *
from issueBook import *
from returnBook import *

root=Tk()
root.title('Library')
root.geometry('1300x700')
img=ImageTk.PhotoImage(file="lib.jpg")
lbl=Label(root,image=img,width=1000,height=450)
lbl.pack()
headFrame=Frame(root,bg="#FFBB00",bd=4)
headFrame.place(x=300,y=10,width=700,height=100)
l=Label(headFrame,text="Welcome to Library",bg='black',fg='white',font=('Courier',18))
l.place(x=20,y=15,width=650,height=60)
b1=Button(lbl,text="Add Book Details",bg='black',fg='white',font=('Courier',14),command=addBooks)
b1.place(x=550,y=200,width=250,height=50)
b2=Button(lbl,text="Delete Book Details",bg='black',fg='white',font=('Courier',14),command=delete)
b2.place(x=550,y=250,width=250,height=50)
b3=Button(lbl,text="View Book Details",bg='black',fg='white',font=('Courier',14),command=View)
b3.place(x=550,y=300,width=250,height=50)
b4=Button(lbl,text="Issue Book to Student",bg='black',fg='white',font=('Courier',14),command=issueBook)
b4.place(x=550,y=350,width=250,height=50)
b5=Button(lbl,text="Return Book",bg='black',fg='white',font=('Courier',14),command=returnBook)
b5.place(x=550,y=400,width=250,height=50)
root.mainloop()
