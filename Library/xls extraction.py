import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='negus', db='library')

cur = db.cursor()


obj = pd.ExcelFile(r'.\Library\libdata.xls')
txtfile = open(r'Sheet1.txt', 'w')
ore = pd.read_excel(r'.\Library\libdata.xls', sheet_name='Sheet2')
'''x = list(ore.values[836])
print(x)
print(type(x))
print(x[5])
if str(x[5]) == 'nan':
    print('yes')
    x[5] = '-'
else:
    print('no')
print(x[5])
print(type(x[5]))'''

'''for i in range(0, 5261):
    x = list(ore.values[i])
    txtfile.write(str(x))
    print(x)'''


# MAIN CODE
for i in range(0, 5261):
    x = list(ore.values[i])
    bookno = int(x[1])
    author = x[2]
    booktitle = x[3]
    publisher = x[4]
    year = x[5]
    cost = x[6]
    type = 'Fiction'

    if str(author) == 'nan':
        author = '-'
    if str(publisher) == 'nan':
        publisher = '-'
    if str(year) == 'nan':
        year = '-'
    if str(cost) == 'nan':
        cost = 0.00

    cur.execute('use library;')
    cur.execute(
        f'''INSERT INTO lib_table VALUES ({bookno},"{str(booktitle)}","{str(author)}","{str(publisher)}","{str(year)}","{str(type)}",{float(cost)});''')
    db.commit()

    print(f'Success (x{i})')
