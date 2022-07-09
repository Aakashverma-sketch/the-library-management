from tkinter import *
from tkinter import messagebox
import mysql.connector
def bookRegister():
    bid=bookinfo1.get()
    title=bookinfo2.get()
    author=bookinfo3.get()
    status=bookinfo4.get()
    con=mysql.connector.connect(host="localhost",user="root",passwd="",database="db1")
    cur=con.cursor()
    try:
        cur.execute("insert into books(bid,title,author,status)values(""+bid+"",""+title+"",""+author+"",""+status+"")")
        con.commit()
        messagebox.showinfo("Success","Book added successfully")
    except:
       messagebox.showinfo("error","cannot add data into database")
    root.destroy()
def addBooks():
    global bookinfo1,bookinfo2,bookinfo3,bookinfo4,root
    root=tk()
    root.title("library")
    root.geometry('1300*700')

    c=canvas(root)
    c.config(bg="#ff6e40")
    c.pack(expand=True,fill=BOTH)
    headFrame1=Frame(root,bg="#FFBB00",bd=4)
    headFrame1.place(x=300,y=10,width=700,height=100)
    l=label(headFrame1,text="Add Books" ,bg="black",fg="white",font=('courier',18))
    l.place(x=20,y=15,width=650,height=60)

    lFrame=Frame(root,bg="black")
    lFrame.place(x=200,y=200,width=900,height=300)


    lb1=label(Frame,text="book ID",bg="black",fg="white",font=('courier',14))
    lb1.place(x=50,y=25,width=300,height=30)
    bookinfo1=Entry(lframe,font=('courier',14))
    bookinfo1.place(x=350,y=25,width=300,height=30)

    lb2=label(Frame,text="title",bg="black",fg="white",font=('courier',14))
    lb2.place(x=50,y=85,width=300,height=30)
    bookinfo2=Entry(lframe,font=('courier',14))
    bookinfo2.place(x=350,y=85,width=300,height=30)

    lb3=label(Frame,text="Author",bg="black",fg="white",font=('courier',14))
    lb3.place(x=50,y=140,width=300,height=30)
    bookinfo2=Entry(lframe,font=('courier',14))
    bookinfo2.place(x=350,y=140,width=300,height=30)

    lb4=label(Frame,text="student(Avail/issued)",bg="black",fg="white",font=('courier',14))
    lb4.place(x=50,y=190,width=300,height=30)
    bookinfo2=Entry(lframe,font=('courier',14))
    bookinfo2.place(x=350,y=190,width=300,height=30)

    b1=button(root,text="SUBMIT",bg="#d1ccc0",fg="black",command=bookRegister)
    b1.place(x=500,y=600,width=80,height=40)

    b2=button(root,text="QUIT",bg="#f711e3",fg="black",command=root.destroy)
    b2.place(x=750,y=600,width=80,height=40)
    root.mainloop()
