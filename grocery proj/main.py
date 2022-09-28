import mysql.connector as mc
import datetime
import hashlib as h
from tabulate import tabulate as table
import sys

db = mc.connect(host='127.0.0.1', user='root', passwd='negus', db='grocery')
cur = db.cursor()


# FUNCTIONS
def itemAvail(itemName):
    cur.execute('select name from item_list;')
    l = cur.fetchall()
    for i in l:
        if str(i[0]).lower() == itemName:
            return True
    else:
        return False


print("\t**** WELCOME TO THE STASH!! ****\n")
name = input(">> Please Enter Your Name:: ")
# --------------------------------ADMIN----------------------------------
if name == 'admin':
    passwd = input('Enter The Password: ')
    if h.sha1(passwd.encode('utf-8')).hexdigest() == 'dc76e9f0c0006e8f919e0c515c66dbba3982f785':

        ques = input('''Enter:
        1) To Add Items. 
        2) To Print History.
        3) To Check Total.
        4) To Quit. \n\n   ==>  ''')

        if ques == '1':
            inpItem = input('Enter Name of Item: ')
            if itemAvail(inpItem):
                inpQuan = input('Add Quantity: ')
                cur.execute(
                    f"""update item_list set quan = quan+{inpQuan} where name = '{inpItem}';""")
                db.commit()

            else:
                inpQuan = int(input('Enter Quantity: '))
                inpPrice = float(input('Enter Price: '))
                cur.execute(
                    f"""insert into item_list(name, quan, price) values('{inpItem}', {inpQuan}, {inpPrice})""")
                db.commit()
            print('\nItem Added Successfully!')

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
        print('Incorrect Password Entered..')


# ------------------------------CUSTOMER---------------------------------
else:
    phno = input(">> Please Enter your Phone Number:: ")
    print(f"\n\t***** Hello {name} *****")
    l = []
    history_l = []
    total = 0
    loop = True

    # list and instructions:
    print('\n>> List Of Available Items <<')
    cur.execute('select name, price, quan from item_list;')
    allItems = []
    for x in cur:
        allItems.append(x)
    print()
    print(table(allItems, headers=['Item', 'Price', 'Quantity']))
    print('\n>> Please Enter "list" for list of Items..')

    while loop:
        item = input('\n>> Enter Name of Item:: ')

        if item.lower() != 'list':
            cur.execute(f"select * from item_list where name = '{item}';")
            ret = cur.fetchone()

            try:
                price = float(ret[3])
                remQuan = float(ret[2])
                quan = int(input('>> Add Quantity:: '))
                if quan <= remQuan:
                    remQuan = remQuan - quan
                    cur.execute(
                        f"update item_list set quan = {remQuan} where name = '{item}';")
                else:
                    print('Not Enough Quantity Present.')
                    continue

                net_price = price * quan
                historyStr = item + f'({quan})'
                history_l.append(historyStr)
                l.append([item, quan, price, net_price])
                total += quan*price

                ques = input('>> Do you wish to Proceed (Y/N):: ')
                if ques.lower() == 'y':
                    continue
                else:
                    loop = False

            except:
                print("__ Item doesn't exist __")
                print('>> Please Enter "list" for list of Items..')
                ques = input('>> Do you wish to Proceed (Y/N):: ')
                if ques.lower() == 'y':
                    pass
                else:
                    loop = False

        if item.lower() == 'list':
            cur.execute('select name, price, quan from item_list;')
            allItems = []
            for x in cur:
                allItems.append(x)
            print()
            print(table(allItems, headers=['Item', 'Price', 'Quantity']))

    print('\n')
    print('\n')

    print('*'*18, 'INVOICE', '*'*18, '\n')

    print(f'Name: {name}')
    print(f'Phone No: {phno}')
    print(f'Date: {datetime.datetime.now().date()}\n')
    print(table(l, headers=['Item', "Quantity", "Price", "Net_Price"]))
    print()
    print('\t    Total:: ', total, '\n')
    print('Thank You For Shopping With Us!')
    print('*'*46)

    # history dump
    cur.execute(
        f'''insert into history(name, phone_no, items, total) values ("{name}", "{phno}", "{history_l}", {total});''')
    db.commit()
