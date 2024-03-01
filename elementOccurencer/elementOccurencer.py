# Prompt the user to enter elements separated by space
input_elements = input("Enter the list elements separated by space: ")

# Convert the input string to a list of integers
elements_list = list(map(int, input_elements.split()))

# Create a dictionary to store the count of each element
element_count = {}

# Count the occurrences of each element in the list
for element in elements_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

# Print the occurrence count of each element
for element, count in element_count.items():
    print(f"{element} occurs {count} {'time' if count == 1 else 'times'}")