from tkinter import Label, font, ttk as t
import mysql.connector
import tkinter as tk
import pyglet
import sys


# DE FUNC NOT USING TKINTER:
old_bookno = 0

# Main tk window init
main = tk.Tk()
main.tk.call("source", r".\\library\\azure.tcl")
main.tk.call("set_theme", "dark")
style = t.Style()

main.title('Library')
main.geometry('1100x700')

db = mysql.connector.connect(
    host='localhost', user='root', password='negus', db='library')

cur = db.cursor()
cur.execute('select * from lib_table;')

# main.rowconfigure(index=0, weight=1)
# main.rowconfigure(index=1, weight=1)
# main.rowconfigure(index=2, weight=1)

pyglet.font.add_file(r'Library\HelveticaNeueMed.ttf')
listofbooks = t.Label(main, text="List Of Books", font=('HelveticaNeue', 42))
listofbooks.grid(row=0, column=0, sticky=('nsew'), padx=30, pady=(60, 30))


# frame creation
entryFrame = t.Labelframe(main, text='Entry', padding=(10, 10, 10, 10))
entryFrame.grid(row=1, column=0, sticky='w',
                padx=(60, 0), rowspan=3, columnspan=4)

# Entry widgets
l_bookno = t.Label(entryFrame, text="Book No:")
l_bookno.grid(row=0, column=0)
e_bookno = t.Entry(entryFrame, width=30)
e_bookno.grid(row=0, column=1, sticky='nsew')

l_booktit = t.Label(entryFrame, text="Book Title:")
l_booktit.grid(row=1, column=0, sticky='nsew', pady=(10, 0))
e_booktit = t.Entry(entryFrame, width=30)
e_booktit.grid(row=1, column=1, sticky='nsew', pady=(10, 0))

l_author = t.Label(entryFrame, text="Author:")
l_author.grid(row=2, column=0, sticky='nsew', pady=(10, 0))
e_author = t.Entry(entryFrame, width=30)
e_author.grid(row=2, column=1, sticky='nsew', pady=(10, 0))


l_publish = t.Label(entryFrame, text="Publisher:")
l_publish.grid(row=0, column=3, sticky='nsew', padx=(20, 0))
e_publish = t.Entry(entryFrame, width=30)
e_publish.grid(row=0, column=4, sticky='nsew')

l_year = t.Label(entryFrame, text="Year:")
l_year.grid(row=1, column=3, sticky='nsew', padx=(20, 0), pady=(10, 0))
e_year = t.Entry(entryFrame, width=30)
e_year.grid(row=1, column=4, sticky='nsew', pady=(10, 0))

l_type = t.Label(entryFrame, text="Type:")
l_type.grid(row=2, column=3, sticky='nsew', padx=(20, 0), pady=(10, 0))
e_type = t.Entry(entryFrame, width=30)
e_type.grid(row=2, column=4, sticky='nsew', pady=(10, 0))


# table frame creation
tableFrame = t.Frame(main)
tableFrame.grid(row=4, column=0, sticky='nsew', padx=60,
                pady=30, columnspan=6, rowspan=7)

# scrollbar creation
scrollbar = t.Scrollbar(tableFrame)
scrollbar.pack(side="right", fill="y")


# table creation
cols = ('bookno', 'booktit', 'author', 'publisher', 'year', 'type', 'price')
table = t.Treeview(tableFrame, columns=cols, show='headings',
                   height=12, yscrollcommand=scrollbar.set)
table.pack(expand=True, fill='both')
scrollbar.config(command=table.yview)


# for i in range(0, 13):
#    ent = t.Entry(main, text='')
#    ent.grid(row=i, column=6)

totbkframe = t.Labelframe(
    main, text='--', padding=(10, 10, 10, 10), width=10, height=10)
totbkframe.grid(row=1, column=4, sticky='nsew', rowspan=3, columnspan=1)


# define headings:
table.heading('bookno', text='Book_No')
table.heading('booktit', text='Book_Title')
table.heading('author', text='Author')
table.heading('publisher', text='Publisher')
table.heading('year', text='Year')
table.heading('type', text='Type')
table.heading('price', text='Price')


table.column('bookno', width=50)
table.column('booktit', width=200)
table.column('author', width=150)
table.column('publisher', width=140)
table.column('year', width=50)
table.column('type', width=110)
table.column('price', width=50)


for x in cur:
    table.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))


# buttons

search_btn = t.Button(main, text='Search', style="big.TButton")
search_btn.grid(row=1, column=6, ipady=10, ipadx=10)

update_btn = t.Button(main, text='Update', style="big.TButton")
update_btn.grid(row=3, column=6, ipady=10, ipadx=10)


clear_btn = t.Button(main, text='Clear', style="big.TButton")
clear_btn.grid(row=4, column=6, ipady=10, ipadx=10, pady=(0, 10))

addition_table_btn = t.Button(main, text='Add Entries', style="big.TButton")
addition_table_btn.grid(row=5, column=6, ipady=10, ipadx=10)

lending_table_btn = t.Button(main, text='Lending Table', style="big.TButton")
lending_table_btn.grid(row=6, column=6, ipady=10, ipadx=10)

quit_btn = t.Button(main, text='Quit', style="big.TButton")
quit_btn.grid(row=7, column=6, ipady=10, ipadx=10)
quit_btn.configure(command=lambda: sys.exit())


tot_l1 = t.Label(totbkframe, text=('Total'), font=('Oswald', 14))
tot_l1.grid(row=0, column=0, sticky='nesw')
tot_l2 = t.Label(totbkframe, text=('Books:'), font=('Oswald', 14))
tot_l2.grid(row=1, column=0, sticky='nsew', pady=8)
tot_l3 = t.Label(totbkframe, font=('Oswald', 14))
tot_l3.grid(row=2, column=0, sticky='nsew')


# FUNCTIONS


def count_update():
    cur.execute('select count(*) from lib_table;')
    for x in cur:
        tot_l3.configure(text=x)


def search():
    ext = ''
    query = 'select * from lib_table where'
    og = query
    if str(e_bookno.get()) != '':
        ext = ext + f' and Book_No = {int(e_bookno.get())}'
    if e_booktit.get() != '':
        if len(e_booktit.get()) == 1:
            ext = ext + f' and Book_Title like "{e_booktit.get()}%"'
        else:
            ext = ext + f' and Book_Title like "%{e_booktit.get()}%"'
    if e_author.get() != '':
        if len(e_author.get()) == 1:
            ext = ext + f' and Author like "{e_author.get()}%"'
        else:
            ext = ext + f' and Author like "%{e_author.get()}%"'

    if e_publish.get() != '':
        if len(e_publish.get()) == 1:
            ext = ext + f' and Publisher like "{e_publish.get()}%"'
        else:
            ext = ext + f' and Publisher like "%{e_publish.get()}%"'
    if e_year.get() != '':
        ext = ext + f' and year = "{e_year.get()}"'
    if e_type.get() != '':
        ext = ext + f' and Type = "{e_type.get()}"'

    query = query + ext
    if query == og:
        q_list = query.split()
        q_list.pop()
        query = ' '.join(q_list)

    else:
        q_list = query.split()
        q_list.pop(5)
        query = ' '.join(q_list)

    query = query + ';'
    print(query)

    cur.execute(query)
    for y in table.get_children():
        table.delete(y)
    for x in cur:
        table.insert('', 'end', values=(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6]))

    count_update()


def sel_ent(event):
    global old_bookno
    for i in table.selection():
        item = table.item(i)
        entry = item['values']

        # deleting
        e_bookno.delete(0, 'end')
        e_booktit.delete(0, 'end')
        e_author.delete(0, 'end')
        e_publish.delete(0, 'end')
        e_year.delete(0, 'end')
        e_type.delete(0, 'end')

        # appending
        e_bookno.insert('end', entry[0])
        e_booktit.insert('end', entry[1])
        e_author.insert('end', entry[2])
        e_publish.insert('end', entry[3])
        e_year.insert('end', entry[4])
        e_type.insert('end', entry[5])
        old_bookno = entry[0]
        print(old_bookno)


def update():
    ext = ''
    global old_bookno
    query = 'update lib_table set'
    og_query = query

    if old_bookno == 0:
        print('nothing to run')
    else:
        if str(e_bookno.get()) != '':
            ext = ext + f', Book_No = {int(e_bookno.get())}'
        if e_booktit.get() != '':
            ext = ext + f', Book_Title = "{e_booktit.get()}"'
        if e_author.get() != '':
            ext = ext + f', Author = "{e_author.get()}"'
        if e_publish.get() != '':
            ext = ext + f', Publisher = "{e_publish.get()}"'
        if e_year.get() != '':
            ext = ext + f', year = "{e_year.get()}"'
        if e_type.get() != '':
            ext = ext + f', Type = "{e_type.get()}"'

        # str modification
        query = query + ext + f' where Book_No = {old_bookno}'
        old_bookno = 0
        if query == og_query:
            print('nothing to do')
        else:
            query_list = query.split()
            field = query_list[2]
            query_list[2] = field[:3]
            query = ' '.join(query_list)
            query = query + ';'
            print(query)
            cur.execute(query)
            db.commit()
            cur.execute('select * from lib_table;')
            for y in table.get_children():
                table.delete(y)
            for x in cur:
                table.insert('', 'end', values=(
                    x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
            count_update()


def clear():
    global old_bookno
    e_bookno.delete(0, 'end')
    e_booktit.delete(0, 'end')
    e_author.delete(0, 'end')
    e_publish.delete(0, 'end')
    e_year.delete(0, 'end')
    e_type.delete(0, 'end')
    search()
    # hardcoding sum shit cos me dumb to do it the right way
    old_bookno = 0


def add_table_func():

    addmain = tk.Tk()
    addmain.tk.call("source", r".\\library\\azure.tcl")
    addmain.tk.call("set_theme", "dark")

    addmain.title('Addition Window')
    addmain.geometry('1100x350')
    add_lbl = t.Label(addmain, text="Enter Your Login Details",
                      font=('HelveticaNeue', 42))
    add_lbl.grid(row=0, column=0, sticky=('nsew'), padx=30, pady=(30, 30))

    btn = t.Button(addmain, text='click', style="big.TButton")
    btn.grid(row=1, column=0, ipady=10, ipadx=10)

    def onClick():
        try:
            cur.execute(
                '''insert into lib_table values (32069, 'emergence', 'mansam', 'tackhiyomi', '2069', 'deep novel', '6.09');''')
            db.commit()
            count_update()
            addmain.destroy()
        except:
            print('Book number is not unique')
            count_update()
            addmain.destroy()

    # config
    btn.configure(command=onClick)
    addmain.mainloop()


# CONFIGUATIONS
search_btn.configure(command=search)
update_btn.configure(command=update)
clear_btn.configure(command=clear)
addition_table_btn.configure(command=add_table_func)


# TREEVIEW FUNCTIONS
table.bind('<<TreeviewSelect>>', sel_ent)


# Styles
style.configure('big.TButton', font=('Oswald', 16))
style.map('big.TButton', foreground=[
          ('active', '#007fff')])

count_update()
main.mainloop()
