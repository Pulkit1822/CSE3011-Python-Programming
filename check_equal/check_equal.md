### Code Snippet: Check if All Elements in List are Equal

#### Function
The code snippet defines a function `check_equal(list1)` to check if all elements in the given list are equal.

#### Inputs
The code snippet doesn't take direct user inputs.

#### Flow
1. The function `check_equal(list1)` compares the list `list1` with its slice from the second element to the last (`list1[1:]`) and its slice from the first element to the second last (`list1[:-1]`).
2. It returns `True` if all elements in the list are equal, otherwise, it returns `False`.

#### Outputs
The code snippet prints the provided lists and the result of checking if all elements in each list are equal using the `check_equal()` function.

```python
# Function to check if all elements in list are equal
def check_equal(list1):
    return list1[1:] == list1[:-1]

# Lists
x = [10, 20, 30, 40, 50]
y = [10, 20, 20, 20, 20]
z = [10, 10, 10, 10, 10]

# Printing lists
print("x:", x)
print("y:", y)
print("z:", z)

# Checking elements
print("check_equal(x):", check_equal(x))
print("check_equal(y):", check_equal(y))
print("check_equal(z):", check_equal(z))
