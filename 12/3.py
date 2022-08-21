# list containing lines which include letter a
ls1 = []

# list containing lines which do not include letter a
ls2 = []

file = open(r'.\12\proj3(1).txt', 'r')
x = file.readlines()

for i in x:
    for k in i:
        if k in 'Aa':
            ls1.append(i)
            break
    else:
        ls2.append(i)
file.close()

# To write in the file containing lines having "Aa"
file = open(r'.\12\proj3(2).txt', 'w')
for i in ls1:
    file.writelines(i)
file.close()

# To write in the file containing lines not having "Aa"
file = open(r'.\12\proj3(3).txt', 'w')
for i in ls2:
    file.writelines(i)
file.close()
