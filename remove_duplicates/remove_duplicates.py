# removing all occurrences of an element from a Python list

# taking input from the user
L = input("Enter list of elements separated by comma: ").split(",")
x = int(input("Enter element to be removed: "))

# converting string to int
L = [int(i) for i in L]

# using list comprehension to remove all occurrences of x from L
result = [i for i in L if i != x]

print(result)

