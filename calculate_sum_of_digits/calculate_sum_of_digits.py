# user input
data = input("Enter the list of numbers separated by comma: ").split(',')

# converting the list to integers
list_data = [int(i) for i in data]

# sum of digits of each number
digit_sums = []
for num in list_data:
    sum_of_digits = 0
    while num > 0:
        digit = num % 10
        sum_of_digits += digit
        num //= 10
    digit_sums.append(sum_of_digits)

# printing the sum of digits
print(digit_sums)