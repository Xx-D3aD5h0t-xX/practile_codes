import csv
import time as t


def returnSeq():
    for i in range(1, 4):
        print(f"\t\t   Returning in {4-i}")
        t.sleep(0.5)


def check(email):
    f = open(r'.\12\pass.csv', 'r', newline='')
    reader = csv.reader(f)
    for i in reader:
        if email == i[0]:
            f.close()
            return True
    else:
        f.close()
        return False


def ret_pass(email):
    f = open(r'.\12\pass.csv', 'r', newline='')
    reader = csv.reader(f)
    for i in reader:
        if email == i[0]:
            return i[1]
    else:
        return False


loop = True
while loop:

    print("\t<<<Welcome to Joe Mama's Password Manager>>>")
    q = input("Enter >> (E)To Add Entries, (P)To See Passwords, (Q)To Quit: ")
    if q.lower() == 'q':
        print("\t<<<Thanks For Using Joe Mama's Password Manager>>>")
        loop = False

    if q.lower() == 'e':
        print('')
        email = input('\t\tEnter Email ID: ')
        if not check(email):
            passwd = input('\t\tEnter Password: ')
            f = open(r'.\12\pass.csv', 'a', newline='')
            writer = csv.writer(f)
            writer.writerow([email, passwd])
            f.close()
            print("\t   <<<Entry Added Successfully>>>")
            returnSeq()

        else:
            print("\t      Email Id Already Exists..")
            returnSeq()

    if q.lower() == 'p':
        email = input('\t\tEnter Email ID: ')
        if ret_pass(email):
            print(f"\t     Password For {email} is: {ret_pass(email)}")
            returnSeq()
        else:
            print(f'\t     No Passwords found for {email}.')
            returnSeq()
