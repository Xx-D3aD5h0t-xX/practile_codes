# Creating an empty dictionary.
dict1 ={}
# Entering total number of students.
n = int(input('Enter the total number of students :'))
# Entering the name, roll number and marks of the students.
for i in range(n):
    ro = int(input('Enter roll number of the student:'))
    na = input('Enter name of the student:')
    ma = int(input('Enter marks of the student:'))
    l = []
    l.append(na)
    l.append(ma)
    k = l
# Code for distinctive entry of roll numbers of the students.	
    if ro in dict1:
        pass
    else:
        dict1[ro] = k
# Printing the created dictionary.
print(dict1)

# Printing the names of the students who got more than 75 marks.
print("-"*60)
print("The names of the students that have more than 75 marks are: ")
for i in dict1:
    if dict1[i][1] >= 75:
        print(dict1[i][0])
    else:
        pass

print("-"*60)






