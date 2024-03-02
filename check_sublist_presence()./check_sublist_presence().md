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
