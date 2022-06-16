from multiprocessing import set_forkserver_preload
from tkinter import ttk as t
import mysql.connector
from ttkthemes import ThemedTk

# Success (x23)
main = ThemedTk(theme='arc')
main.title('Library')
main.geometry('850x700')

db = mysql.connector.connect(
    host='localhost', user='root', password='negus', db='library')

cur = db.cursor()
cur.execute('select * from lib_table;')


cols = ('bookno', 'booktit', 'author', 'publisher', 'year', 'type')
table = t.Treeview(main, columns=cols, show='headings', height=19)
#table.place(x=30, y=30)
table.grid(row=0, column=0, sticky='ns', padx=5, pady=5)

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


# table.insert('', 'end',
#             values=('Jai', "M", '17'))


#btn = t.Button(main, text='Click')
#btn.place(x=400, y=250)


# scrollbar creation
scrollbar = t.Scrollbar(main, orient='vertical', command=table.yview)
table.configure(yscroll=scrollbar.set)
#scrollbar.place(x=331, y=30)
scrollbar.grid(row=0, column=1, sticky='ns')


main.mainloop()
