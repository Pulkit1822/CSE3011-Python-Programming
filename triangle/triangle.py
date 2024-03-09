side1 = int(input("Enter the 1st side: "))
side2 = int(input("Enter the 2nd side: "))
side3 = int(input("Enter the 3rd side: "))
if side1 == side2 == side3:
        print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
else:
        print("Scalene triangle")

