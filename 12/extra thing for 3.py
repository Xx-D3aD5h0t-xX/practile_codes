file = open(r'.\12\proj3.txt', 'r')
x = ''
r = file.readlines()
for i in r:
    w = i.strip()
    x = x+w
z = x.split('.')

file.close()
file = open(r'.\12\proj3(1).txt', 'w')
for i in z:
    i = i.lstrip()
    print(i)
    file.writelines(i+'.\n')
file.close()
