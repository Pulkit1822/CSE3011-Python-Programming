# Python program to print Fibonacci series

# take input from the user
n = int(input("How many terms? "))

# first two terms
a = 0
b = 1

count = 0
while count < n:
   print(a, end=' ')
   a, b = b, a + b
   count += 1

# end the program
print()

