import random
a = "y"
while a == "y":
    print('\n<<The Random Number Generated Is>>\n')
    x = random.randint(1, 6)
    print(f'<<             {x}             >>\n')

    a = input("Would you like to continue(y/n)?: ")



