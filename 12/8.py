import csv

def check(email):
    f = open(r'.\pass.csv', 'r', newline='')
    reader = csv.reader(f)
    for i in reader:
        if email == i[0]:
            f.close()
            return True
    else:
        f.close()
        return False


def ret_pass(email):
    f = open(r'.\pass.csv', 'r', newline='')
    reader = csv.reader(f)
    for i in reader:
        if email == i[0]:
            return i[1]
    else:
        return False

loop = True
while loop:

    q = input("Enter >> (E)To Add Entries, (P)To See Passwords, (Q)To Quit: ")
    if q.lower() == 'q':
        print("\t<<<Thanks For Using Password Manager>>>")
        loop = False

    if q.lower() == 'e':
        print('')
        email = input('\t\tEnter Email ID: ')
        if not check(email):
            passwd = input('\t\tEnter Password: ')
            f = open(r'.\pass.csv', 'a', newline='')
            writer = csv.writer(f)
            writer.writerow([email, passwd])
            f.close()
            print("\t   <<<Entry Added Successfully>>>\n")

        else:
            print("\t      Email Id Already Exists..\n")

    if q.lower() == 'p':
        email = input('\t\tEnter Email ID: ')
        if ret_pass(email):
            print(f"\t     Password For {email} is: {ret_pass(email)}\n")

        else:
            print(f'\t     No Passwords found for {email}.\n')
