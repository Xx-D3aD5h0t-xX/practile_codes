from multiprocessing import set_forkserver_preload
from tkinter import ttk as t
import mysql.connector as sql
from ttkthemes import ThemedTk


main = ThemedTk(theme='arc')
main.title('Library')
main.geometry('850x700')


cols = ('name', 'sex', 'age')
table = t.Treeview(main, columns=cols, show='headings', height=19)
table.place(x=30, y=30)

# define headings:
table.heading('name', text='Name')
table.heading('sex', text='Sex')
table.heading('age', text='Age')
table.column('name', width=90)
table.column('sex', width=90)
table.column('age', width=90)


table.insert('', 'end',
             values=('Jai', "M", '17'))

table.insert("", 'end', text="L1",
             values=("Nidhi", "F", "25"))
table.insert("", 'end', text="L2",
             values=("Nisha", "F", "23"))
table.insert("", 'end', text="L3",
             values=("Preeti", "F", "27"))
table.insert("", 'end', text="L4",
             values=("Rahul", "M", "20"))
table.insert("", 'end', text="L5",
             values=("Sonu", "F", "18"))
table.insert("", 'end', text="L6",
             values=("Rohit", "M", "19"))
table.insert("", 'end', text="L7",
             values=("Geeta", "F", "25"))
table.insert("", 'end', text="L8",
             values=("Ankit", "M", "22"))
table.insert("", 'end', text="L10",
             values=("Mukul", "F", "25"))
table.insert("", 'end', text="L11",
             values=("Mohit", "M", "16"))
table.insert("", 'end', text="L12",
             values=("Vivek", "M", "22"))
table.insert("", 'end', text="L13",
             values=("Suman", "F", "30"))


btn = t.Button(main, text='Click')
btn.place(x=130, y=300)


main.mainloop()
