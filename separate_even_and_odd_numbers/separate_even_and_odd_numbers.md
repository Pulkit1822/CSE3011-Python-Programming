### Code Snippet: Even and Odd Numbers Separator

#### Inputs
The code snippet prompts the user to enter elements separated by spaces.

#### Flow
1. The code snippet takes input from the user, expecting a list of elements separated by spaces.
2. It converts the input string to a list of integers.
3. It initializes two empty lists: `even_numbers` and `odd_numbers`.
4. It iterates through the list of numbers and appends even numbers to the `even_numbers` list and odd numbers to the `odd_numbers` list.
5. It prints the lists containing even and odd numbers, respectively.

#### Outputs
The code snippet outputs two lists: one containing even numbers and the other containing odd numbers from the entered list.

```python
# Getting input from the user
L = [int(x) for x in input("Enter elements separated by space: ").split()]

even_numbers = list()
odd_numbers = list()

# Separating even and odd numbers
for i in L:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

# Printing even and odd numbers
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
