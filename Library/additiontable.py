from tkinter import Label, font, ttk as t
import mysql.connector
import tkinter as tk
import pyglet
import sys


def dababy():
    # db init
    db = mysql.connector.connect(
        host='localhost', user='root', password='negus', db='library')

    cur = db.cursor()

    # main window init
    addmain = tk.Tk()
    addmain.tk.call("source", r".\\library\\azure.tcl")
    addmain.tk.call("set_theme", "dark")
    style = t.Style()

    addmain.title('Addition Window')
    addmain.geometry('1100x350')

    btn = t.Button(addmain, text='click', style="big.TButton")
    btn.grid(row=1, column=6, ipady=10, ipadx=10)

    def onClick():
        cur.execute(
            '''insert into lib_table values (32069, 'emergence', 'mansam', 'tackhiyomi', '2069', 'deep novel', '6.09');''')
        db.commit()

    # config
    btn.configure(command=onClick)

    # Styles
    style.configure('big.TButton', font=('Oswald', 16))
    style.map('big.TButton', foreground=[
              ('active', '#007fff')])

    addmain.mainloop()
