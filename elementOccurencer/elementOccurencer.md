### Code Snippet: Element Occurrence Counter

#### Inputs
The code snippet prompts the user to enter elements separated by space.

#### Flow
1. The code snippet takes input from the user, expecting elements separated by spaces.
2. It converts the input string into a list of integers.
3. It initializes an empty dictionary `element_count` to store the count of each element.
4. It iterates through the elements in the list and updates the count in the dictionary accordingly.
5. It prints the occurrence count of each element along with the element itself.

#### Outputs
The code snippet outputs the count of occurrences for each element entered by the user.

```python
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
