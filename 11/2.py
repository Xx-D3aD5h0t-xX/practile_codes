l = [0,1,2,3,4,5,6,7,8,9,10]
le = []
lo = []
length = len(l)

for i in range(0, length):
    if i % 2 == 0:
        le.append(l[i])
    else:
        lo.append(l[i])

l1 = []
for i in range(len(lo)):
    l1.append(lo[i])
    l1.append(le[i])
if length/2 != 0 :
	l1.append(l[-1])
else : 
	pass
print("Default List:", l)
print("After Modifying:", l1)
        


