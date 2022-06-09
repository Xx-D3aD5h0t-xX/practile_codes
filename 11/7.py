Side1 = int(input("Enter length of side : "))
Side2 = int(input("Enter length of side : "))
Side3 = int(input("Enter length of side : "))
if Side1 == Side2 and Side2 == Side3 and Side3 == Side1:
 print("The triangle is equilateral  ")
elif Side1 == Side2 or Side2 == Side3 or Side3 == Side1:
 print("The triangle is isosceles")
else:
    print("the triangle is scalene")

