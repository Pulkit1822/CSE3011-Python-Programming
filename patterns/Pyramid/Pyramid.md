## Summary
This code generates a pattern of starred pyramids based on user input.

## Example Usage
```python
How many starred pyramids do you want: 3
  *
 * *
* * *
```

## Code Analysis
### Inputs
- `star_count`: an integer representing the number of starred pyramids the user wants to generate.
___
### Flow
1. Prompt the user to enter the number of starred pyramids they want.
2. Iterate over each row in the range of `star_count`.
3. For each row, iterate over each column in the range of `star_count - row - 1` and print a space.
4. For each row, iterate over each column in the range of `row + 1` and print a star followed by a space.
5. Print a new line after each row.
___
### Outputs
- A pattern of starred pyramids based on the user input.
___
