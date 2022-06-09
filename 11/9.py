# User Input
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))

# HCF
CF = []
HCF = 0

# X
HCF_X = []
for a in range(1,x+1):
    if x%a == 0:
        HCF_X.append(a)
# Y
HCF_Y = []
for b in range(1,y+1):
    if y%b == 0:
        HCF_Y.append(b)
# CF (Common Factor)
for i in HCF_X:
    for j in HCF_Y:
        if i == j:
            CF.append(i)

HCF = max(CF)
print("The Highest Common Factor(HCF) of {} and {} is: {}".format(x, y, HCF))


# LCM
LCM = int((x*y)/HCF)
print("The Least Common Multiple(LCM) of {} and {} is: {}".format(x, y, LCM))


    

