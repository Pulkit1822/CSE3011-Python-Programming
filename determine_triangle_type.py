def determine_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

if __name__ == "__main__":
    sides = input("Enter the lengths of the three sides of the triangle, separated by spaces: ").split()
    sides = [int(side) for side in sides]
    determine_triangle_type(*sides)
