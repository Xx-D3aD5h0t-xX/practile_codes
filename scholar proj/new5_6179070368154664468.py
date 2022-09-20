# the gui for scholar project
from tkinter import *
'''from PIL import ImageTk,Image'''
from tkinter import colorchooser  # sub module
from tkinter import messagebox as mb

import mysql.connector
sql = mysql.connector.connect(
    host="localhost", user="root", passwd="negus", database="scholar")
cursor = sql.cursor()


def RegisterScholar():
    a = f2.get()  # roll.no    int
    b = f3.get()  # address   varchar
    c = f4.get()   # name  varchar
    d = f5.get()  # city     varchar
    e = f6.get()   # class    int
    f = f7.get()   # ph no  varchar
    g = f8.get()   # age int
    h = f9.get()  # reg fee  int
    try:
        cursor.execute("insert into scholar(roll,address,name,city,class,phone,age,regfee) values({},'{}','{}','{}',{},'{}',{},{})".format(
            a, b, c, d, e, f, g, h))
        sql.commit()
        f2.delete(0, END)
        f3.delete(0, END)
        f4.delete(0, END)
        f5.delete(0, END)
        f6.delete(0, END)
        f7.delete(0, END)
        f8.delete(0, END)
        f9.delete(0, END)
        mb.showinfo("Success", "Scholar Added.")

    except:
        mb.showerror("Error", "Scholar Couldn't be Added.")


def ShowResult():
    r = cursor.fetchall()
    for i in r:
        return(i)


def RemoveScholar():  # removing scholar function
    e = e11.get()
    if e == '':
        mb.showerror("Error", "Roll No field can't be Empty.")
    else:
        cursor.execute('select * from scholar where roll={}'.format(e))

        if cursor.fetchall() == []:
            mb.showerror("Error", "Roll No doesn't Exist.")
        else:
            cursor.execute("delete from scholar where roll={}".format(e))
            sql.commit()
            e11.delete(0, END)
            mb.showinfo("Success", "Scholar Removed Successfully.")

# search scholar functions


def search1():
    n = str(e13.get())    # str instead of eval
    cursor.execute("select * from scholar where name='{}'".format(n))
    r = ShowResult()
    e13.delete(0, END)
    res.configure(text=str(r))


def search2():
    n = str(e15.get())
    cursor.execute("select * from scholar where city = '{}'".format(n))
    r = ShowResult()
    e15.delete(0, END)
    res.configure(text=str(r))


def search3():
    n = eval(e14.get())
    cursor.execute("select * from scholar where age={}".format(n))
    r = ShowResult()
    e14.delete(0, END)
    res.configure(text=str(r))


def search4():
    n = eval(e16.get())
    cursor.execute("select * from scholar where class = {}".format(n))
    r = ShowResult()
    e16.delete(0, END)
    res.configure(text=str(r))


def search5():
    n = eval(e17.get())
    cursor.execute("select * from scholar where phone= '{}'".format(n))
    r = ShowResult()
    e17.delete(0, END)
    res.configure(text=str(r))


def search6():
    n = eval(e18.get())
    cursor.execute("select * from scholar where address = '{}'".format(n))
    r = ShowResult()
    e18.delete(0, END)
    res.configure(text=str(r))


def search7():
    n = eval(e19.get())
    cursor.execute("select * from scholar where regfee = {}".format(n))
    r = ShowResult()
    e19.delete(0, END)
    res.configure(text=str(r))


def search8():
    n = eval(e12.get())
    cursor.execute("select * from scholar where roll={}".format(n))
    r = ShowResult()
    e12.delete(0, END)
    res.configure(text=str(r))


win = Tk()
win.title("SCHOLAR")
win.geometry("750x750")
win.configure(bg="#efd3f5")

l1 = Label(win, text=' .-.-.-.-.-.-.-.-.-.- SCHOLAR MANAGEMENT SYSTEM -.-.-.-.-.-.-.-.-.-.-.',
           background="black", foreground="white", font=("algerian", 20))
l1.place(x=2, y=2)


#labels and buttons
l = Label(win, text="SCHOLAR REGISTRATION ZONE", font=(
    "Arial"), foreground="#de0a6f", background="#ffff80")
l.place(x=2, y=40)

l2 = Label(win, text="ROLL NO.")
l2.place(x=2, y=70)
f2 = Entry(win)
f2.place(x=75, y=70)

l3 = Label(win, text="ADDRESS")
l3.place(x=250, y=70)
f3 = Entry(win)
f3.place(x=370, y=70)

l4 = Label(win, text=" NAME")
l4.place(x=2, y=100)
f4 = Entry(win)
f4.place(x=75, y=100)

l5 = Label(win, text="CITY")
l5.place(x=250, y=100)
f5 = Entry(win)
f5.place(x=370, y=100)

l6 = Label(win, text="CLASS")
l6.place(x=2, y=130)
f6 = Entry(win)
f6.place(x=75, y=130)

l7 = Label(win, text="PHONE NO.")
l7.place(x=250, y=130)
f7 = Entry(win)
f7.place(x=370, y=130)

l8 = Label(win, text="AGE")
l8.place(x=2, y=160)
f8 = Entry(win)
f8.place(x=75, y=160)

l9 = Label(win, text="REGISTRATION FEE")
l9.place(x=250, y=160)
f9 = Entry(win)
f9.place(x=370, y=160)

b1 = Button(win, command=RegisterScholar, text="REGISTER",
            background='#65b1b1').place(x=500, y=160)

l10 = Label(win, text="REMOVE SCHOLAR HERE", font=("Arial"),
            foreground="#de0a6f", background="#ffff80")
l10.place(x=2, y=225)

l11 = Label(win, text=" ENTER ROLL NO")
l11.place(x=267, y=228)
e11 = Entry(win)
e11.place(x=375, y=228)
b2 = Button(win, text="REMOVE", command=RemoveScholar,
            background='cyan').place(x=510, y=225)

l10 = Label(win, text="SEARCH SCHOLARS", font=("Arial"),
            foreground="#de0a6f", background="#ffff80")
l10.place(x=2, y=275)

l20 = Label(win, text="REQUIRED RECORD", font=("Arial"), background="green")
l20.place(x=500, y=275)

res = Label(win, text="SCHOLAR")
res.place(x=500, y=400)


l12 = Label(win, text="SEARCH SCHOLAR VIA ROLL NO HERE")
l12.place(x=2, y=300)
e12 = Entry(win)
e12.place(x=250, y=300)
b3 = Button(win, text="SEARCH", command=search8,
            background='#fab830').place(x=375, y=300)

l13 = Label(win, text="SEARCH SCHOLAR VIA NAME HERE")
l13.place(x=2, y=330)
e13 = Entry(win)
e13.place(x=250, y=330)
b4 = Button(win, text="SEARCH", command=search1,
            background='#fab830').place(x=375, y=330)

l14 = Label(win, text="SEARCH SCHOLAR VIA AGE HERE")
l14.place(x=2, y=360)
e14 = Entry(win)
e14.place(x=250, y=360)
b5 = Button(win, text="SEARCH", command=search3,
            background='#fab830').place(x=375, y=360)

l15 = Label(win, text="SEARCH SCHOLAR VIA CITY HERE")
l15.place(x=2, y=390)
e15 = Entry(win)
e15.place(x=250, y=390)
b6 = Button(win, text="SEARCH", command=search2,
            background='#fab830').place(x=375, y=390)

l16 = Label(win, text="SEARCH SCHOLAR VIA CLASS HERE")
l16.place(x=2, y=420)
e16 = Entry(win)
e16.place(x=250, y=420)
b7 = Button(win, text="SEARCH", command=search4,
            background='#fab830').place(x=375, y=420)

l17 = Label(win, text="SEARCH SCHOLAR VIA PHONE NO HERE")
l17.place(x=2, y=450)
e17 = Entry(win)
e17.place(x=250, y=450)
b8 = Button(win, text="SEARCH", command=search5,
            background='#fab830').place(x=375, y=450)

l18 = Label(win, text="SEARCH SCHOLAR VIA ADDRESS HERE")
l18.place(x=2, y=480)
e18 = Entry(win)
e18.place(x=250, y=480)
b9 = Button(win, text="SEARCH", command=search6,
            background='#fab830').place(x=375, y=480)

l19 = Label(win, text="SEARCH SCHOLAR VIA FEE HERE")
l19.place(x=2, y=510)
e19 = Entry(win)
e19.place(x=250, y=510)
b10 = Button(win, text="SEARCH", command=search7,
             background='#fab830').place(x=375, y=510)

'''canvas = Canvas(win, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("ball.png"))  
canvas.create_image(700, 60, anchor=NW, image=img)'''


win.mainloop()
