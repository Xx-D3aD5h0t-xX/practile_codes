# the gui for scholar project
from tkinter import *
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


def searchRes(tup):
    # making all entries editable
    se1.configure(state=NORMAL)
    se2.configure(state=NORMAL)
    se3.configure(state=NORMAL)
    se4.configure(state=NORMAL)
    se5.configure(state=NORMAL)
    se6.configure(state=NORMAL)
    se7.configure(state=NORMAL)
    se8.configure(state=NORMAL)

    # deleting all the prev inserted entries
    se1.delete(0, END)
    se2.delete(0, END)
    se3.delete(0, END)
    se4.delete(0, END)
    se5.delete(0, END)
    se6.delete(0, END)
    se7.delete(0, END)
    se8.delete(0, END)

    # inserting values
    se1.insert(1, tup[0])
    se2.insert(1, tup[1])
    se3.insert(1, tup[2])
    se4.insert(1, tup[3])
    se5.insert(1, tup[4])
    se6.insert(1, tup[5])
    se7.insert(1, tup[6])
    se8.insert(1, tup[7])

    # making entries uneditable
    se1.configure(state=DISABLED)
    se2.configure(state=DISABLED)
    se3.configure(state=DISABLED)
    se4.configure(state=DISABLED)
    se5.configure(state=DISABLED)
    se6.configure(state=DISABLED)
    se7.configure(state=DISABLED)
    se8.configure(state=DISABLED)

# bug fixing


def disableEntries():
    se1.configure(state=DISABLED)
    se2.configure(state=DISABLED)
    se3.configure(state=DISABLED)
    se4.configure(state=DISABLED)
    se5.configure(state=DISABLED)
    se6.configure(state=DISABLED)
    se7.configure(state=DISABLED)
    se8.configure(state=DISABLED)


def search1():
    try:
        n = str(e13.get())    # str instead of eval
        cursor.execute("select * from scholar where name='{}'".format(n))
        r = ShowResult()
        e13.delete(0, END)
    except:
        disableEntries()


def search2():
    try:
        n = str(e15.get())
        cursor.execute("select * from scholar where city = '{}'".format(n))
        r = ShowResult()
        e15.delete(0, END)
        searchRes(r)
    except:
        disableEntries()


def search3():
    try:
        n = eval(e14.get())
        cursor.execute("select * from scholar where age={}".format(n))
        r = ShowResult()
        e14.delete(0, END)
        searchRes(r)

    except:
        disableEntries()


def search4():
    try:
        n = eval(e16.get())
        cursor.execute("select * from scholar where class = {}".format(n))
        r = ShowResult()
        e16.delete(0, END)
        searchRes(r)
    except:
        disableEntries()


def search5():
    try:
        n = eval(e17.get())
        cursor.execute("select * from scholar where phone= '{}'".format(n))
        r = ShowResult()
        e17.delete(0, END)
        searchRes(r)
    except:
        disableEntries()


def search6():
    try:
        n = eval(e18.get())
        cursor.execute("select * from scholar where address = '{}'".format(n))
        r = ShowResult()
        e18.delete(0, END)
        searchRes(r)
    except:
        disableEntries()


def search7():
    try:
        n = eval(e19.get())
        cursor.execute("select * from scholar where regfee = {}".format(n))
        r = ShowResult()
        e19.delete(0, END)
        searchRes(r)
    except:
        disableEntries()


def search8():
    try:
        n = eval(e12.get())
        cursor.execute("select * from scholar where roll={}".format(n))
        r = ShowResult()
        e12.delete(0, END)
        searchRes(r)

    except:
        disableEntries()


win = Tk()
win.title("SCHOLAR")
win.geometry("750x550")
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
l10.place(x=2, y=265)

l20 = Label(win, text="REQUIRED RECORD", font=("Arial"), background="green")
l20.place(x=500, y=265)

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

# labels for search menu
sl1 = Label(win, text='ROLL NO.')
sl1.place(x=500, y=300)

sl2 = Label(win, text='NAME.')
sl2.place(x=500, y=330)

sl3 = Label(win, text='AGE')
sl3.place(x=500, y=360)

sl4 = Label(win, text='CITY')
sl4.place(x=500, y=390)

sl5 = Label(win, text='CLASS')
sl5.place(x=500, y=420)

sl6 = Label(win, text='PHONE NO.')
sl6.place(x=500, y=450)

sl7 = Label(win, text='ADDRESS')
sl7.place(x=500, y=480)

sl8 = Label(win, text='REG. FEE')
sl8.place(x=500, y=510)

# result labels

se1 = Entry(win, width=17)
se1.place(x=590, y=300)
se1.configure(state=DISABLED)


se2 = Entry(win, width=17)
se2.place(x=590, y=330)
se2.configure(state=DISABLED)

se3 = Entry(win, width=17)
se3.place(x=590, y=360)
se3.configure(state=DISABLED)

se4 = Entry(win, width=17)
se4.place(x=590, y=390)
se4.configure(state=DISABLED)

se5 = Entry(win, width=17)
se5.place(x=590, y=420)
se5.configure(state=DISABLED)

se6 = Entry(win, width=17)
se6.place(x=590, y=450)
se6.configure(state=DISABLED)

se7 = Entry(win, width=17)
se7.place(x=590, y=480)
se7.configure(state=DISABLED)

se8 = Entry(win, width=17)
se8.place(x=590, y=510)
se8.configure(state=DISABLED)

win.mainloop()
