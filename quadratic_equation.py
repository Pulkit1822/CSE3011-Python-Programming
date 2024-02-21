import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return (root,)
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

if __name__ == "__main__":
    print("Enter the coefficients of the quadratic equation (ax^2 + bx + c):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    roots = find_roots(a, b, c)
    
    if len(roots) == 1:
        print(f"The quadratic equation has one real root: {roots[0]}")
    elif isinstance(roots[0], complex):
        print(f"The quadratic equation has two complex roots: {roots[0]} and {roots[1]}")
    else:
        print(f"The quadratic equation has two real roots: {roots[0]} and {roots[1]}")
