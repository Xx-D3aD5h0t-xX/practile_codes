# Entering the element.
ele = input("Enter the element : ")

print("-"*45)
# Checking if the element is a palindrome.
if(ele == ele[: : -1]):
    print(f"The Element {ele} is a palindrome")
else:
    print(f"The Element {ele} is not a palindrome")
print("-"*45)


