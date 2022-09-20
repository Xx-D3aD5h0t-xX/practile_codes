import pickle
emp1 = {"rollno": 101, "name": "student1", "Marks": 94}
emp2 = {"rollno": 102, "name": "student2", "Marks": 89}
emp3 = {"rollno": 103, "name": "student3", "Marks": 84}
emp4 = {"rollno": 104, "name": "student4", "Marks": 90}
emp5 = {"rollno": 105, "name": "student5", "Marks": 80}
emp6 = {"rollno": 106, "name": "student6", "Marks": 79}
emp7 = {"rollno": 107, "name": "student7", "Marks": 88}
emp8 = {"rollno": 108, "name": "student8", "Marks": 96}
myfile = open(r"./student.dat", "wb")
pickle.dump(emp1, myfile)
pickle.dump(emp2, myfile)
pickle.dump(emp3, myfile)
pickle.dump(emp4, myfile)
pickle.dump(emp5, myfile)
pickle.dump(emp6, myfile)
pickle.dump(emp7, myfile)
pickle.dump(emp8, myfile)
print("Successfully Updated")
myfile.close()

user = int(input("Enter Roll No you want to search: "))
marks = int(input("Update the marks: "))
try:
    myfile = open(r"./student.dat", "rb+")
    while True:
        temp = myfile.tell()
        a = pickle.load(myfile)
        if a["rollno"] == user:
            myfile.seek(temp)
            a["Marks"] = marks
            pickle.dump(a, myfile)
        print(a)
except FileNotFoundError:
    print("Please check the file name")
except EOFError:
    myfile.close()


    
