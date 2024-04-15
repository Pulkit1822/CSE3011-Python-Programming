## Summary
This function prints a pyramid pattern of numbers based on the number of rows specified.

## Example Usage
```python
print_pyramid(5)
```

## Code Analysis
### Inputs
- `rows`: an integer representing the number of rows in the pyramid.
___
### Flow
1. Iterate through each row from 1 to the specified number of rows.
2. For each row, iterate through each column from 1 to the difference between the total number of rows and the current row number.
3. Print a space for each column to create the left indentation of the pyramid.
4. For each row, iterate through each column from 1 to twice the current row number.
5. Print the current row number for each column to create the pyramid pattern.
6. Move to the next line after each row is printed.
___
### Outputs
- None (prints the pyramid pattern directly to the console).
___
