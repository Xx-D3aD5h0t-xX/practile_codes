import pickle
myfile = open(r".\stu.dat", "ab+")
a = {}
found = True
while found :
    roll = int(input("Enter the Roll Number: "))
    name = input("Enter the Name: ")
    a[roll]= name
    pickle.dump(a, myfile)
    opt = input('Do you want to enter more Roll Numbers: (y/n)')
    if opt == 'y':
      pass
    elif opt == 'n' :
      found = False
myfile.seek(0)
c = int(input("Enter the Roll Number to search: "))
try:
    while True:
        b = pickle.load(myfile)
        if c in b:
            print("Roll No. of",b[c],"is: ",c)
            found = False
        else :
        	  found = True
except :
    if not found:
        myfile.close()
    else:
        print("Student details not found.")
        myfile.close()



