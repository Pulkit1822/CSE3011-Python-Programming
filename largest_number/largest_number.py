num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is largest")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is largest")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is largest")
else:
    print(f"{num4} is largest")