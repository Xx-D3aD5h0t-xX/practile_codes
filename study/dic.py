import mysql.connector as m

db = m.connect(host='localhost', user='root', passwd='negus', db='library')

cur = db.cursor()
cur.execute('SELECT * FROM lib_table where Book_No < 10;')

x = cur.fetchone()
print(x)

cur.execute('SELECT * FROM lib_table where Book_No < 10;')

y = cur.fetchall()
print(y)
