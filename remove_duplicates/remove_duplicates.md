### Code Snippet: Remove Duplicates from List

#### Inputs
The code snippet prompts the user to enter a list of elements separated by space.

#### Flow
1. The code snippet takes input from the user, expecting a string of elements separated by spaces.
2. It converts the input string into a list of strings.
3. It converts the list of strings into a list of integers.
4. It creates a set from the list to remove duplicate elements.
5. It converts the set back to a list to retain the distinct elements.
6. It prints the list containing only the distinct elements.

#### Outputs
The code snippet outputs a list with duplicate elements removed.

```python
# getting the input from the user
data = input("Enter the list elements separated by space: ")

# converting the string to list
list_data = data.split()

# converting the list to integers
list_data = [int(i) for i in list_data]

# creating a set to remove the duplicates
unique_set = set(list_data)

# converting the set back to list
distinct_list = list(unique_set)

# printing the list
print(distinct_list)
