## Summary
This code snippet removes all occurrences of a given element from a Python list.

## Example Usage
```python
Enter list of elements separated by comma: 1,2,3,4,5
Enter element to be removed: 3
[1, 2, 4, 5]
```

## Code Analysis
### Inputs
- `L`: A list of elements entered by the user, separated by commas.
- `x`: The element to be removed from the list.
___
### Flow
1. The user is prompted to enter a list of elements and the element to be removed.
2. The input list is converted from a string to a list of integers.
3. List comprehension is used to create a new list (`result`) that contains all elements from the input list (`L`) except for the element to be removed (`x`).
4. The `result` list is printed.
___
### Outputs
- `result`: A new list that contains all elements from the input list except for the element to be removed.
___
