import random

loop = True
while loop:
    inp = input("Roll The Dice(y,n): ")
    if inp == "y":
        x = random.randint(1, 6)
        print("-"*40)
        print("The Output Of The Dice Is: {}.".format(x))
        print("-"*40)
    else:
        print("Thanks For Using!")
        loop = False
        

