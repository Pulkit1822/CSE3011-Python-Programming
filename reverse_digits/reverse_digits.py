# Prompt the user to input an integer
num = int(input("Enter an integer: "))

# Initialize variables
reversed_num = 0

# Reverse the digits of the input number
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

# Output the reversed number
print("Reversed number:", reversed_num)
