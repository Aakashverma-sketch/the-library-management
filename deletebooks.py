from tkinter import*
from tkinter import messagebox
import mysql.connector
def deleteBook():
    con=mysql.connector.connect(host="localhost",user="root",passwd="iics",database="db1")
    cur=con.cursor()
    bid=boolinfo1.get()
    try:
        cur.execute("delete from books where bid="+bid+"")
        con.commit()
        messagebox.showinfo("Success","Book Record deleted successfully")
    except:
        messagebox.showinfo("Error","Please check Book ID")
def delete():
    root=Tk()
    root.title("Library")
    root.geometry('1300x700')

    global bookinfo1
    c=Canvas(root)
    c.config(bg="#006B38")
    c.pack(expand=True,fill=BOTH)
    headFrame1=Frame(root,bg="#FFBBOO",bd=4)
    headFrame1.place(x=300,y=10,width=700,height=100)
    l=Label(headFrame1,text="Delete Books",bg="black",fg="white",font('Courier',18))
    l.place(x20,y=15,width=650,height=60)

    lFrame=Frame(root.bg="black")
    lFrame.place(x=200,y=200,width=900,height=300)

    lb1=Label(lFrame,text"Book ID",bg="black",fg="white",font=('courier',14))
    lb1.place(x=50,y=100,width=300,height=30)
    bookinfo1=Entry(lFrame,font('Courier',14))
    bookinfo1.place(x=350,y=100,width=300,height=30)

    b1=Button(root,text="SUBMIT",bg="#d1ccc0",fg="black",command=deleteBook)
    b1.place(x=500,y=600,width=80,height=40)

    b2=Button(root,text="OUIT",bg="#f7f1e3",fg="black",command=root.destroy)
    b2.place(x=750,y=600,width=80,height=40)
    root.mainloop()
