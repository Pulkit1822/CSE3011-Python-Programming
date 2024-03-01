## Summary
The `maxMin` function takes a list as input and returns the maximum and minimum values in the list.

## Example Usage
```python
myList = [5, 2, 9, 1, 7]
max_val, min_val = maxMin(myList)
print(max_val)  # Output: 9
print(min_val)  # Output: 1
```

## Code Analysis
### Inputs
- `myList` (list): The input list of numbers.
___
### Flow
1. Check if the input list is empty. If it is, return `None` for both the maximum and minimum values.
2. Initialize the variables `maximum` and `minimum` with the first element of the list.
3. Iterate over the remaining elements of the list.
4. If an element is greater than the current maximum, update the `maximum` variable.
5. If an element is smaller than the current minimum, update the `minimum` variable.
6. After iterating through all the elements, return the `maximum` and `minimum` values.
___
### Outputs
- `maximum` (number): The maximum value in the input list.
- `minimum` (number): The minimum value in the input list.
___
