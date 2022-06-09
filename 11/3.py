lst1 = []
new_lst = int(input("Enter number of elements : "))

for i in range(new_lst):
    value = input("Enter element : ")
    lst1.append(value)
print("The entered list is :" , lst1)

n = int(input("Enter the number you want to search :"))

length = len(lst1)
for i in range(length):
    if n == int(lst1[i]):
        print(f"The element {n} is present at index : {i} ")
        break
else:
    print(f"The element {n} is not present in the list")
    
    
    




        
