my_file=open(r"./proj2.txt","r")
vow=con=up=lc=0
b=my_file.read()

for i in b:
    if i.isalpha():
        if i in ['a','e','i','o','u','A','E','I','O','U'] :
            vow+=1
        else:
            con+=1
    if i.isupper():
        up+=1
    elif i.islower():
        lc+=1

print('Original String:', b)
print("No. Of Vowels",vow)
print("No. Of Consonants",con)
print("No. Of UpperCase",up)
print("No. Of LowerCase",lc)





