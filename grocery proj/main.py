import mysql.connector as mc
import getpass as gp
import datetime
import hashlib as h
from tabulate import tabulate as table
import sys

db = mc.connect(host='127.0.0.1', user='root', passwd='negus', db='grocery')
cur = db.cursor()


# FUNCTIONS


print("**** WELCOME TO THE STASH!! ****\n")
name = input(">> Please Enter Your Name:: ")
# --------------------------------ADMIN----------------------------------
if name == 'admin':
    passwd = gp.getpass(prompt=">> Please Enter the Password: ")
    if h.sha1(passwd.encode('utf-8')).hexdigest() == 'e346f201d9272e2ea204e5128e5205193dd1afe6':
        print('como estas nigro')
        ques = input('''Enter:
        1) To Add Items. 
        2) To Print History.
        3) To Check Total.
        4) To Quit. \n\n   ==>  ''')

        if ques == '1':
            pass
        if ques == '2':
            l = []
            cur.execute('select * from history;')
            for x in cur:
                l.append(x)
            print()
            print(
                table(l, headers=["Name", "Phone_No", "Date", "Items", "Total"]))
        if ques == '3':
            tot = 0
            cur.execute('select total from history;')
            for x in cur:
                tot += float(x[0])
            print(f'\n Total Income :: {tot} \n')
        else:
            sys.exit()
    else:
        print('gtfo')


# ------------------------------CUSTOMER---------------------------------
else:
    phno = input(">> Please Enter your Phone Number:: ")
    print(f"\n***** Hello {name} *****")
    l = []
    history_l = []
    total = 0
    loop = True
    while loop:
        item = input('\n>> Enter Name of Item:: ')

        if item.lower() != 'list':
            cur.execute(f"select * from item_list where name = '{item}';")
            price = cur.fetchone()

            try:
                price = float(price[2])
                quan = int(input('>> Add Quantity:: '))
                cum_price = price * quan
                historyStr = item + f'({quan})'
                history_l.append(historyStr)
                l.append([item, quan, price, cum_price])
                total += quan*price

                ques = input('>> Do you wish to Proceed (Y/N):: ')
                if ques.lower() == 'y':
                    continue
                else:
                    loop = False

            except:
                print("__ Item doesn't exist __")
                print('>>Please Enter "list" for list of Items..')
                ques = input('>> Do you wish to Proceed (Y/N):: ')
                if ques.lower() == 'y':
                    pass
                else:
                    loop = False

        if item.lower() == 'list':
            cur.execute('select name, price from item_list;')
            allItems = []
            for x in cur:
                allItems.append(x)
            print()
            print(table(allItems, headers=['Item', 'Price']))

    print('\n')
    print('\n')

    print('*'*18, 'INVOICE', '*'*18, '\n')

    print(f'Name: {name}')
    print(f'Phone No: {phno}')
    print(f'Date: {datetime.datetime.now().date()}\n')
    print(table(l, headers=['Item', "Quantity", "Price", "Cum_Price"]))
    print()
    print('\t    Total:: ', total, '\n')
    print('Thank You For Shopping With Us!')
    print('*'*46)

    # history dump
    cur.execute(
        f'''insert into history(name, phone_no, items, total) values ("{name}", "{phno}", "{history_l}", {total});''')
    db.commit()
