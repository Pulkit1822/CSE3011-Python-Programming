# Taking input from the user for the number of elements
number_of_elements = int(input("Enter number of elements: "))
elements_list = []

# Appending elements to the list
for _ in range(number_of_elements):
    element = int(input("Enter an element: "))
    elements_list.append(element)

# Calculating the sum of all elements
total_sum = 0
for item in elements_list:
    total_sum += item

# Printing the sum
print("Sum of all elements:", total_sum)