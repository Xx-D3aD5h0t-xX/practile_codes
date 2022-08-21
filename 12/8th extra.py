from pickle import *

#init_file = open(r'pass.txt', 'wb')
# dump({1: 'ad'}, init_file)
# init_file.close()

init_file = open(r'.\12\pass.txt', 'r+b')
try:
    x = load(init_file)
    init_file.close()
except:
    print('File was empty')
    dump({}, init_file)
    init_file.close()
init_file.close()


def update(uid, pas):
    re = open(r'.\12\pass.txt', 'rb')

    try:
        x = load(re)
        re.close()
        x[uid] = pas
        wr = open(r'.\12\pass.txt', 'wb')
        dump(x, wr)
        wr.close()
    except:
        pass


def getkeys():
    try:
        f = open(r'.\12\pass.txt', 'rb')
        x = load(f)
        f.close()
        return (list(x.keys()))

    except:
        pass


def getvalues():
    try:
        f = open(r'.\12\pass.txt', 'r+b')
        f.seek(0, 0)
        x = load(f)
        f.close()
        return (list(x.values()))

    except:
        pass


ques = input('Enter UID (Type "show" for saved passwords): ')

if ques != 'show':
    if ques != getkeys():
        passwd = input(f'Enter Password for {ques}: ')
        update(ques, passwd)
    else:
        print('That UID already exists.')

else:
    for i in range(0, len(getkeys())):
        print(f'UID: {getkeys()[i]} :: PASS: {getvalues()[i]}')
