## Summary
The code snippet checks if a given list contains a given sub list.

## Example Usage
```python
Enter the list of numbers separated by space: 1 2 3 4 5
Enter the sub list of numbers separated by space: 3 4
YES
```

## Code Analysis
### Inputs
- `list_data`: a list of numbers entered by the user.
- `sub_list`: a sub list of numbers entered by the user.
___
### Flow
1. The user is prompted to enter a list of numbers.
2. The input is split into individual numbers and converted to integers.
3. The user is prompted to enter a sub list of numbers.
4. The input is split into individual numbers and converted to integers.
5. A variable `contains_sublist` is initialized as `False`.
6. A loop iterates through the main list to find the sub list.
7. If the sub list is found, `contains_sublist` is set to `True` and the loop is terminated.
8. The result is printed as "YES" if `contains_sublist` is `True`, otherwise "NO".
___
### Outputs
- "YES" if the main list contains the sub list.
- "NO" if the main list does not contain the sub list.
___

## Purpose
The purpose of this code snippet is to demonstrate how to check if a given list contains a sub list in Python. It allows the user to input a list and a sub list, and then determines whether the main list contains the sub list. This is a fundamental operation in Python programming and is useful for understanding how to work with lists and loops.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `check_sublist_presence.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python check_sublist_presence.py
   ```
5. Follow the prompt to enter a list of numbers and a sub list of numbers. The code will determine if the main list contains the sub list and print the result.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter a list of numbers and a sub list of numbers. For example:
```python
Enter the list of numbers separated by space: 1 2 3 4 5
Enter the sub list of numbers separated by space: 3 4
YES
```
In this example, the user enters the list of numbers `1 2 3 4 5` and the sub list of numbers `3 4`. The code determines that the main list contains the sub list and prints "YES" as the output.
