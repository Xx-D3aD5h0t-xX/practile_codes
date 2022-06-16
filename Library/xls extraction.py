import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='negus', db='library')

cur = db.cursor()

#file_loc = r"C:\Users\St. Mary's Lab\Desktop\Git Repos\practile_codes\Library\libdata.xls"
ore = pd.read_excel(r'Library\\libdata.xls', sheet_name='Sheet22')
x = list(ore.values[0])


# MAIN CODE
for i in range(0, 5248):
    x = list(ore.values[i])
    bookno = int(x[1])
    author = x[2]
    booktitle = x[3]
    publisher = x[4]
    year = x[5]
    cost = x[6]
    type = 'Competitive Exams'

    if str(author) == 'nan':
        author = '-'
    if str(publisher) == 'nan':
        publisher = '-'
    if str(year) == 'nan':
        year = '-'
    if str(cost) == 'nan':
        cost = 0.00

    cur.execute('use library;')
    try:
        cur.execute(
            f'''INSERT INTO lib_table VALUES ({bookno},"{str(booktitle)}","{str(author)}","{str(publisher)}","{str(year)}","{str(type)}",{float(cost)});''')
        db.commit()
    except mysql.connector.errors.DataError:
        year = int(x[5])
        cur.execute(
            f'''INSERT INTO lib_table VALUES ({bookno},"{str(booktitle)}","{str(author)}","{str(publisher)}","{str(year)}","{str(type)}",{float(cost)});''')
        db.commit()
    print(f'Success (x{i})')
