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
This program works as follows:

1. It prompts the user to input an integer.
2. It initializes a variable reversed_num to 0.
3. It enters a while loop, which continues as long as num is greater than 0.
4. Inside the loop, it calculates the last digit of num using the modulus operator (%), and adds this digit to reversed_num after shifting its current digits one place to the left (multiplying by 10).
5. It then removes the last digit from num using integer division (//).
6. Once all digits have been processed (i.e., num is no longer greater than 0), it prints the reversed number.