from tkinter import DISABLED, ttk as t
import mysql.connector
import tkinter as tk
import pyglet
import sys
from tkinter import messagebox


# DE FUNC NOT USING TKINTER:
old_bookno = 0


# Main tk window init
main = tk.Tk()
main.tk.call("source", r".\\library\\azure.tcl")
main.tk.call("set_theme", "dark")
style = t.Style(master=main)

main.title('Library')
main.geometry('1100x720')
main.resizable(False, False)

db = mysql.connector.connect(
    host='127.0.0.1', username='root', password='negus', db='library')

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
                padx=(60, 0), rowspan=4, columnspan=4)

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

l_price = t.Label(entryFrame, text="Price:")
l_price.grid(row=3, column=0, sticky='nsew', pady=(10, 0))
e_price = t.Entry(entryFrame, width=30)
e_price.grid(row=3, column=1, sticky='nsew', pady=(10, 0))


l_shelf = t.Label(entryFrame, text="shelf:")
l_shelf.grid(row=3, column=3, sticky='nsew', padx=(20, 0), pady=(10, 0))
e_shelf = t.Entry(entryFrame, width=30)
e_shelf.grid(row=3, column=4, sticky='nsew', pady=(10, 0))


# table frame creation
tableFrame = t.Frame(main)
tableFrame.grid(row=5, column=0, sticky='nsew', padx=60,
                pady=15, columnspan=6, rowspan=7)

# scrollbar creation
scrollbar = t.Scrollbar(tableFrame)
scrollbar.pack(side="right", fill="y")


# table creation
cols = ('bookno', 'booktit', 'author', 'publisher',
        'year', 'type', 'price', 'shelf')
table = t.Treeview(tableFrame, columns=cols, show='headings',
                   height=12, yscrollcommand=scrollbar.set)
table.pack(expand=True, fill='both')
scrollbar.config(command=table.yview)


# for i in range(0, 13):
#    ent = t.Entry(main, text='')
#    ent.grid(row=i, column=6)

totbkframe = t.Labelframe(
    main, text='--', padding=(10, 10, 10, 10), width=10, height=4)
totbkframe.grid(row=1, column=4, sticky='nsew', rowspan=4, columnspan=1)


# define headings:
table.heading('bookno', text='Book_No')
table.heading('booktit', text='Book_Title')
table.heading('author', text='Author')
table.heading('publisher', text='Publisher')
table.heading('year', text='Year')
table.heading('type', text='Type')
table.heading('price', text='Price')
table.heading('shelf', text='Shelf')


table.column('bookno', width=50, anchor="center")
table.column('booktit', width=190, anchor="center")
table.column('author', width=140, anchor="center")
table.column('publisher', width=120, anchor="center")
table.column('year', width=50, anchor="center")
table.column('type', width=110, anchor="center")
table.column('price', width=50, anchor="center")
table.column('shelf', width=40, anchor="center")


for x in cur:
    table.insert('', 'end', values=(
        x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))


# buttons

search_btn = t.Button(main, text='Search', style="big.TButton")
search_btn.grid(row=1, column=6, ipady=20, ipadx=10)

update_btn = t.Button(main, text='Update', style="big.TButton")
update_btn.grid(row=2, column=6, ipady=20, ipadx=10, pady=(10, 0))


clear_btn = t.Button(main, text='Clear', style="big.TButton")
clear_btn.grid(row=5, column=6, ipady=10, ipadx=10, pady=(0, 0))

addition_table_btn = t.Button(main, text='Add Entries', style="big.TButton")
addition_table_btn.grid(row=7, column=6, ipady=10, ipadx=10)

lending_table_btn = t.Button(main, text='Lending Table', style="big.TButton")
lending_table_btn.grid(row=8, column=6, ipady=10, ipadx=10)

quit_btn = t.Button(main, text='Quit', style="big.TButton")
quit_btn.grid(row=9, column=6, ipady=10, ipadx=10)
quit_btn.configure(command=lambda: sys.exit())


tot_l1 = t.Label(totbkframe, text=('Total'), font=('Oswald', 14))
tot_l1.grid(row=0, column=0, sticky='nesw')
tot_l4 = t.Label(totbkframe, text=('Number Of'), font=('Oswald', 14),)
tot_l4.grid(row=1, column=0, sticky='nsew', pady=(8, 0))
tot_l2 = t.Label(totbkframe, text=('Books:'), font=('Oswald', 14))
tot_l2.grid(row=2, column=0, sticky='nsew', pady=8)
tot_l3 = t.Label(totbkframe, font=('Oswald', 14))
tot_l3.grid(row=3, column=0, sticky='nsew')


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

    # NEW ENTRIES
    # ---------------OPTIONAL CODE FOR PRICE-----------------
    # if e_price.get() != '':
        # if len(e_price.get()) == 1:
        # ext = ext + f' and price like "{e_price.get()}%"'
        # else:
        # ext = ext + f' and price like "%{e_price.get()}%"'
    if e_price.get() != '':
        ext = ext + f' and price = "{e_price.get()}"'

    if e_shelf.get() != '':
        if len(e_shelf.get()) == 1:
            ext = ext + f' and shelf like "{e_shelf.get()}%"'
        else:
            ext = ext + f' and shelf like "%{e_shelf.get()}%"'

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
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))

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
        e_price.delete(0, 'end')
        e_shelf.delete(0, 'end')

        # appending
        e_bookno.insert('end', entry[0])
        e_booktit.insert('end', entry[1])
        e_author.insert('end', entry[2])
        e_publish.insert('end', entry[3])
        e_year.insert('end', entry[4])
        e_type.insert('end', entry[5])
        e_price.insert('end', entry[6])
        e_shelf.insert('end', entry[7])

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
        if e_price.get() != '':
            ext = ext + f', price = "{e_price.get()}"'
        if e_shelf.get() != '':
            ext = ext + f', shelf = "{e_shelf.get()}"'

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
                    x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
            count_update()


def clear():
    global old_bookno
    e_bookno.delete(0, 'end')
    e_booktit.delete(0, 'end')
    e_author.delete(0, 'end')
    e_publish.delete(0, 'end')
    e_year.delete(0, 'end')
    e_type.delete(0, 'end')
    e_price.delete(0, 'end')
    e_shelf.delete(0, 'end')
    search()
    # hardcoding sum shit cos me dumb to do it the right way
    # fk this shit, this is the right way..
    old_bookno = 0


def add_table_func():

    addmain = tk.Tk()
    addmain.tk.call("source", r".\\library\\azure.tcl")
    addmain.tk.call("set_theme", "dark")

    # checkbutton vars
    check_bookno = tk.IntVar(master=addmain, value=0)
    check_author = tk.IntVar(master=addmain)
    check_publish = tk.IntVar(master=addmain)
    check_year = tk.IntVar(master=addmain)
    check_type = tk.IntVar(master=addmain)
    check_price = tk.IntVar(master=addmain)

    addmain.title('Addition Window')
    addmain.geometry('1070x370')
    style = t.Style(master=addmain)
    addmain.resizable(False, False)

    add_lbl = t.Label(addmain, text="Add Entries:",
                      font=('HelveticaNeue', 35))
    add_lbl.grid(row=0, column=0, sticky=('nsew'), padx=30, pady=(30, 30))

    frame = t.Labelframe(addmain, text='joe', padding=(10, 10, 10, 10))
    frame.grid(row=1, column=0, padx=(50, 0), sticky=(
        'nsew'), rowspan=4, columnspan=6)

    # entry widgets

    bktitframe = t.Frame(frame)
    bktitframe.grid(row=0, column=0, rowspan=1, columnspan=6, pady=(0, 10))
    la_booktit = t.Label(bktitframe, text="Book Title:")
    la_booktit.grid(row=0, column=0)
    ea_booktit = t.Entry(bktitframe, width=90)
    ea_booktit.grid(row=0, column=1, padx=(10, 0), sticky='nsew')

    la_bookno = t.Label(frame, text="Book No:")
    la_bookno.grid(row=1, column=0, sticky='nsew', pady=(10, 0))
    ea_bookno = t.Entry(frame, width=30)
    ea_bookno.grid(row=1, column=1, sticky='nsew')
    ca_bookno = t.Checkbutton(frame, variable=check_bookno, state='disabled')
    ca_bookno.grid(row=1, column=2)

    la_author = t.Label(frame, text="Author:")
    la_author.grid(row=2, column=0, sticky='nsew', pady=(10, 0))
    ea_author = t.Entry(frame, width=30)
    ea_author.grid(row=2, column=1, sticky='nsew', pady=(10, 0))
    ca_author = t.Checkbutton(
        frame, variable=check_author, offvalue=0, onvalue=1)
    ca_author.grid(row=2, column=2, pady=(10, 0))

    la_publish = t.Label(frame, text="Publisher:")
    la_publish.grid(row=3, column=0, sticky='nsew', pady=(10, 0))
    ea_publish = t.Entry(frame, width=30)
    ea_publish.grid(row=3, column=1, sticky='nsew', pady=(10, 0))
    ca_publish = t.Checkbutton(
        frame, variable=check_publish, offvalue=0, onvalue=1)
    ca_publish.grid(row=3, column=2, pady=(10, 0))

    la_year = t.Label(frame, text="Year:")
    la_year.grid(row=1, column=3, sticky='nsew')
    ea_year = t.Entry(frame, width=30)
    ea_year.grid(row=1, column=4, sticky='nsew')
    ca_year = t.Checkbutton(frame, variable=check_year, offvalue=0, onvalue=1)
    ca_year.grid(row=1, column=5)

    la_type = t.Label(frame, text="Type:")
    la_type.grid(row=2, column=3, sticky='nsew', pady=(10, 0))
    ea_type = t.Entry(frame, width=30)
    ea_type.grid(row=2, column=4, sticky='nsew', pady=(10, 0))
    ca_type = t.Checkbutton(frame, variable=check_type, offvalue=0, onvalue=1)
    ca_type.grid(row=2, column=5, pady=(10, 0))

    la_price = t.Label(frame, text="Price:")
    la_price.grid(row=3, column=3, sticky='nsew', pady=(10, 0))
    ea_price = t.Entry(frame, width=30)
    ea_price.grid(row=3, column=4, sticky='nsew', pady=(10, 0))
    ca_price = t.Checkbutton(
        frame, variable=check_price, offvalue=0, onvalue=1)
    ca_price.grid(row=3, column=5, pady=(10, 0))

    # button
    addbtn = t.Button(addmain, text='Add', style="big.TButton")
    addbtn.grid(row=1, column=6, padx=(40, 0),
                ipadx=20, ipady=15, pady=(10, 10))

    quitbtn = t.Button(addmain, text='Quit', style="big.TButton")
    quitbtn.grid(row=3, column=6, padx=(40, 0),
                 ipadx=20, ipady=15, pady=(10, 0))

    def onAdd():
        if ea_booktit.get() != '' and ea_bookno.get() != '' and ea_author.get() != '' and ea_publish.get() != '' and ea_year.get() != '' and ea_type.get() != '' and ea_price.get() != '':
            try:
                print('YEAS')
                cur.execute(
                    f'''insert into lib_table values ({int(ea_bookno.get())}, '{ea_booktit.get()}', '{ea_author.get()}', '{ea_publish.get()}', '{ea_year.get()}', '{ea_type.get()}', '{ea_price.get()}');''')
                db.commit()

                ea_booktit.delete(0, 'end')
                ea_bookno.delete(0, 'end')

                if check_author.get() == 0:
                    ea_author.delete(0, 'end')
                if check_publish.get() == 0:
                    ea_publish.delete(0, 'end')
                if check_year.get() == 0:
                    ea_year.delete(0, 'end')
                if check_type.get() == 0:
                    ea_type.delete(0, 'end')
                if check_price.get() == 0:
                    ea_price.delete(0, 'end')

                messagebox.showinfo(
                    title='Success', message='The Entry Was Successfully Added.')
                addmain.lift()
                count_update()

            except mysql.connector.errors.IntegrityError:
                print('Book number is not unique')
                messagebox.showerror("Error", "The Book Number Is Not Unique.")
                addmain.lift()
                count_update()

            except:
                print('The Values entered are Incorrect')
                messagebox.showerror(
                    "Error", "The Values Entered Are Incorrect.")
                addmain.lift()
                count_update()

        else:
            print('no shit')

    def debugbtn():
        print(check_author.get(), check_publish,
              check_year, check_type, check_price)

    # button configs.get()
    # quitbtn.configure(command=debugbtn)
    quitbtn.configure(command=lambda: addmain.destroy())
    addbtn.configure(command=onAdd)

    # Style config
    style.configure('big.TButton', font=('Oswald', 16))
    style.map('big.TButton', foreground=[
        ('active', '#007fff')])

    # end
    addmain.mainloop()


def lending_table_func():
    # lending table gui init
    lendmain = tk.Tk()
    lendmain.tk.call("source", r".\\library\\azure.tcl")
    lendmain.tk.call("set_theme", "dark")
    lendmain.title('Lending Table')
    lendmain.geometry('1200x720')
    style = t.Style(master=lendmain)
    lendmain.resizable(False, False)

    # Checkbutton vars
    check_lost = tk.IntVar(master=lendmain)

    # MAIN
    lend_lbl = t.Label(lendmain, text="Lending Table:",
                       font=('HelveticaNeue', 42))
    lend_lbl.grid(row=0, column=0, sticky=('nsew'), padx=30, pady=(60, 30))

    entryFrame = t.Labelframe(lendmain, text='Entry', padding=(10, 10, 10, 10))
    entryFrame.grid(row=1, column=0, sticky='w',
                    padx=(60, 0), rowspan=4, columnspan=5)

    # Entry widgets
    bktitframe = t.Frame(entryFrame)
    bktitframe.grid(row=0, column=0, rowspan=1, columnspan=4, pady=(0, 10))
    l_booktit = t.Label(bktitframe, text="Book Title:")
    l_booktit.grid(row=0, column=0, sticky='nsew', pady=(10, 0))
    e_booktit = t.Entry(bktitframe, width=85)
    e_booktit.grid(row=0, column=1, sticky='nsew', pady=(10, 0))

    l_bookno = t.Label(entryFrame, text="Book No:")
    l_bookno.grid(row=1, column=0, sticky='nsew', pady=(10, 0))
    e_bookno = t.Entry(entryFrame, width=25)
    e_bookno.grid(row=1, column=1, sticky='nsew', pady=(10, 0))

    l_stuname = t.Label(entryFrame, text="Student Name:")
    l_stuname.grid(row=1, column=2, sticky='nsew', pady=(10, 0), padx=(20, 0))
    e_stuname = t.Entry(entryFrame, width=25)
    e_stuname.grid(row=1, column=3, sticky='nsew', pady=(10, 0))

    l_roll = t.Label(entryFrame, text="Roll No:")
    l_roll.grid(row=2, column=0, sticky='nsew', pady=(10, 0))
    e_roll = t.Entry(entryFrame, width=25)
    e_roll.grid(row=2, column=1, sticky='nsew', pady=(10, 0))

    l_class = t.Label(entryFrame, text="Class:")
    l_class.grid(row=2, column=2, sticky='nsew', pady=(10, 0), padx=(20, 0))
    e_class = t.Entry(entryFrame, width=25)
    e_class.grid(row=2, column=3, sticky='nsew', pady=(10, 0))

    l_date = t.Label(entryFrame, text="Date Of Borrowing:")
    l_date.grid(row=3, column=0, sticky='nsew', pady=(10, 0))
    e_date = t.Entry(entryFrame, width=25)
    e_date.grid(row=3, column=1, sticky='nsew', pady=(10, 0))

    l_leftdays = t.Label(entryFrame, text="Days Left:")
    l_leftdays.grid(row=3, column=2, sticky='nsew', pady=(10, 0), padx=(20, 0))
    e_leftdays = t.Entry(entryFrame, width=25)
    e_leftdays.grid(row=3, column=3, sticky='nsew', pady=(10, 0))

    l_fine = t.Label(entryFrame, text="Fine:")
    l_fine.grid(row=4, column=0, sticky='nsew', pady=(10, 0), padx=(20, 0))
    e_fine = t.Entry(entryFrame, width=25)
    e_fine.grid(row=4, column=1, sticky='nsew', pady=(10, 0))

    l_lost = t.Label(entryFrame, text="Is Lost:")
    l_lost.grid(row=4, column=2, sticky='nsew', pady=(10, 0), padx=(20, 0))
    c_lost = t.Checkbutton(
        entryFrame, variable=check_lost, offvalue=0, onvalue=1)
    c_lost.grid(row=4, column=3, sticky='nsew', pady=(10, 0), padx=(90, 0))

    # End
    lendmain.mainloop()


# CONFIGUATIONS
search_btn.configure(command=search)
update_btn.configure(command=update)
clear_btn.configure(command=clear)
addition_table_btn.configure(command=add_table_func)
lending_table_btn.configure(command=lending_table_func)


# TREEVIEW FUNCTIONS
table.bind('<<TreeviewSelect>>', sel_ent)


# Styles
style.configure('big.TButton', font=('Oswald', 16))
style.map('big.TButton', foreground=[
          ('active', '#007fff')])


# addition_table_btn.invoke()

count_update()
main.mainloop()
