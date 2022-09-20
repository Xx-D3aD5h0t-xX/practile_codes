# list containing lines which do not include letter a
ls1 = []

file = open(r'.\proj3(1).txt', 'r')
x = file.readlines()

for i in x:
    for k in i:
        if k in 'Aa':
            break
    else:
        ls1.append(i)
file.close()

# To write in the file containing lines not having "Aa"
file = open(r'.\proj3(2).txt', 'w')
for i in ls1:
    file.writelines(i)
file.close()



