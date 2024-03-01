## Summary
The `isSorted` function checks if a given list is sorted in ascending order.

## Example Usage
```python
myList = [1, 2, 3, 4, 5]
print(isSorted(myList))
# Output: True

myList = [5, 4, 3, 2, 1]
print(isSorted(myList))
# Output: False
```

## Code Analysis
### Inputs
- `myList` (list): The input list to be checked for sorting.
___
### Flow
1. Iterate through the elements of the input list using a for loop.
2. Compare each element with the next element in the list.
3. If any element is greater than the next element, return False.
4. If the loop completes without finding any out-of-order elements, return True.
___
### Outputs
- `True` if the input list is sorted in ascending order.
- `False` if the input list is not sorted in ascending order.
___
