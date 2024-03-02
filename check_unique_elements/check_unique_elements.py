# Taking input from the user for the number of elements
number_of_elements = int(input("Enter number of elements: "))
unique_elements_list = []

# Appending elements to the list
for _ in range(number_of_elements):
    element = int(input("Enter an element: "))
    if element not in unique_elements_list:
        unique_elements_list.append(element)

# Checking if all the elements are unique
if len(unique_elements_list) == number_of_elements:
    print("All elements are unique")
else:
    print("Not all elements are unique")

