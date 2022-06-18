from tkinter import Label, font, ttk as t
import mysql.connector
import tkinter as tk
import pyglet

# DE FUNC NOT USING TKINTER:


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
                pady=30, columnspan=6, rowspan=4)

# scrollbar creation
scrollbar = t.Scrollbar(tableFrame)
scrollbar.pack(side="right", fill="y")


# table creation
cols = ('bookno', 'booktit', 'author', 'publisher', 'year', 'type')
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


# buttons


search_btn = t.Button(main, text='Search', style="big.TButton")
search_btn.grid(row=1, column=6, ipady=10, ipadx=10,
                pady=(0, 10))

update_btn = t.Button(main, text='Update', style="big.TButton")
update_btn.grid(row=3, column=6, ipady=10, ipadx=10)


# define headings:
table.heading('bookno', text='Book_No')
table.heading('booktit', text='Book_Title')
table.heading('author', text='Author')
table.heading('publisher', text='Publisher')
table.heading('year', text='Year')
table.heading('type', text='Type')

table.column('bookno', width=60)
table.column('booktit', width=200)
table.column('author', width=150)
table.column('publisher', width=150)
table.column('year', width=50)
table.column('type', width=130)

for x in cur:
    table.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))


tot_l1 = t.Label(totbkframe, text=('Total'), font=('Oswald', 14))
tot_l1.grid(row=0, column=0, sticky='nesw')
tot_l2 = t.Label(totbkframe, text=('Books:'), font=('Oswald', 14))
tot_l2.grid(row=1, column=0, sticky='nsew', pady=8)
tot_l3 = t.Label(totbkframe, font=('Oswald', 14))
tot_l3.grid(row=2, column=0, sticky='nsew')


# TREEVIEW FUNCTIONS


# FUNCTIONS


def count_update():
    cur.execute('select count(*) from lib_table;')
    for x in cur:
        tot_l3.configure(text=x)


def idk():
    if e_type.get() == '':
        print('NOTHING AT ALL NIGGER')
        cur.execute('select * from lib_table;')
        for y in table.get_children():
            table.delete(y)
        for x in cur:
            table.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
        count_update()

    else:
        print('Fk this shit nigger')
        cur.execute('select * from lib_table where year = "1972";')
        for y in table.get_children():
            table.delete(y)
        for x in cur:
            table.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
        count_update()


def search():
    ext = ''
    query = 'select * from lib_table where'
    og = query
    if str(e_bookno.get()) != '':
        ext = ext + f' and Book_No = {int(e_bookno.get())}'
    if e_booktit.get() != '':
        ext = ext + f' and Book_Title = "{e_booktit.get()}"'
    if e_author.get() != '':
        ext = ext + f' and Author = "{e_author.get()}"'
    if e_publish.get() != '':
        ext = ext + f' and Publisher = "{e_publish.get()}"'
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
            x[0], x[1], x[2], x[3], x[4], x[5]))

    count_update()


def update():
    query = 'update lib_table set'


# CONFIGUATIONS
search_btn.configure(command=search)


# Styles
style.configure('big.TButton', font=('Oswald', 16))
style.map('big.TButton', foreground=[
          ('active', '#007fff')])

count_update()
main.mainloop()
