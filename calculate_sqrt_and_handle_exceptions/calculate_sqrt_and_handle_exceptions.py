import math

try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")
    result = math.sqrt(number)
    with open("sqrt_results.txt", "w") as file:
        file.write(f"The square root of {number} is {result}")
    print(f"The square root of {number} is {result}")
except ValueError as e:
    print(f"Error: {e}")
    