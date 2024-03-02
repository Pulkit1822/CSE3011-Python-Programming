largest = None
smallest = None

while True:
    num = int(input("Enter a number(To stop press 0): "))
    if num == 0:
        break

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print(f"Smallest number entered is {smallest}")
print(f"Largest number entered is = {largest}")

