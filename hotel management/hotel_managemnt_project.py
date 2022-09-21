import mysql.connector

mycon = mysql.connector.connect(
    host="localhost", user="root", passwd="negus", database="hotel_management")
cursor = mycon.cursor()


def add_customer():
    print('''Welcome to hotel Prayagraj and Sons!!! \n''')
    a1 = input("Enter customer id ")
    a2 = input("Enter name ")
    a3 = input("Enter phone number ")
    a4 = input("Enter address ")
    a5 = input("Enter email ")
    cursor.execute("insert into c_details values(%s,%s,%s,%s,%s)",
                   (a1, a2, a3, a4, a5))
    mycon.commit()


def show_all():
    cursor.execute("select * from c_details")
    x = cursor.fetchall()
    print(("ID", "Name", "Phone", "Address", "E-mail"))
    for i in x:
        print(i)


def select_service():
    e = input(''' Welcome !!! \n
    Enter 1 for room \n
    Enter 2 for restaurant \n
    Enter 3 for pool \n
    ''')
    if e == 1:
        room()
    elif e == 2:
        restaurant()
    elif e == 3:
        pool()


def restaurant():
    print('''Welcome to restaurant !!\n
    1. Veg combo - 300 \n
    2. Non veg combo - 500 \n
    3. Chinese - 800\n
    4. Italian - 700 \n
    5. Russian - 600\n''')
    e = int(input("Enter choice "))
    eid = input("Enter customer id ")
    if e == 1:
        cursor.execute(
            "update booking_record set restaurant = %s where c_id = %s", (300, eid))
        mycon.commit()
    elif e == 2:
        cursor.execute(
            "update booking_record set restaurant = %s where c_id = %s", (500, eid))
        mycon.commit()
    elif e == 3:
        cursor.execute(
            "update booking_record set restaurant = %s where c_id = %s", (800, eid))
        mycon.commit()
    elif e == 4:
        cursor.execute(
            "update booking_record set restaurant = %s where c_id = %s", (700, eid))
        mycon.commit()

    elif e == 4:
        cursor.execute(
            "update booking_record set restaurant = %s where c_id = %s", (600, eid))
        mycon.commit()


def pool():
    n = input(''' Welcome to pool !! \n
    Price = Rs. 1000
    Enter ID of customer. \n ''')
    cursor.execute(
        "update booking_record set pool = pool + 1000 where c_id = '{}'".format(n))
    mycon.commit()
    cursor.execute("update booking_record set total = total + pool")
    mycon.commit()


def room():
    print(''' Welcome!!! \n
    Please select room type : \n
    1. Royal - 3500 \n
    2. Deluxe - 2500 \n
    3. Standard - 2000 \n
    4. Budget - 1000 \n''')
    e = int(input("Enter choice "))
    eid = input("Enter customer id ")
    if e == 1:
        cursor.execute(
            "update booking_record set room = %s where c_id = %s", (3000, eid))
        mycon.commit()
    elif e == 2:
        cursor.execute(
            "update booking_record set room = %s where c_id = %s", (2500, eid))
        mycon.commit()
    elif e == 3:
        cursor.execute(
            "update booking_record set room = %s where c_id = %s", (2000, eid))
        mycon.commit()
    elif e == 4:
        cursor.execute(
            "update booking_record set room = %s where c_id = %s", (1000, eid))
        mycon.commit()


def view_bill():
    n = input("Enter customer id\n")
    cursor.execute("update booking_record set total = restaurant+pool+room")
    mycon.commit()
    cursor.execute("select total from booking_record where c_id = %s", (n))
    e = cursor.fetchone()
    print("Bill for customer", n, "is as follows : \n")
    print(e)


def see_customer():
    e = input("Enter id of customer ")
    cursor.execute("select * from c_details where c_id = %s", (e))
    i = cursor.fetchall()
    print("ID", "Name", "Phone", "Address", "E-mail")
    print(i)


c = True
while c == True:
    e = int(input('''
    Press 1 for adding customer \n
    Press 2 to view all customers \n
    Press 3 for services \n
    Press 4 to view bill of customer\n
    Press 5 to view specific customer details \n
    Press 6 to end program \n'''))
    if e == 1:
        add_customer()
    elif e == 2:
        show_all()
    elif e == 3:
        select_service()
    elif e == 4:
        view_bill()
    elif e == 5:
        see_customer()
    elif e == 6:
        c = False
