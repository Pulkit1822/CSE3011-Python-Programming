## Summary
This function finds the largest and smallest numbers among a given set of numbers.

## Example Usage
```python
find_smallest_and_largest(5)
```
Enter a number: 10
Enter a number: 5
Enter a number: 8
Enter a number: 3
Enter a number: 12
The largest number is: 12
The smallest number is: 3

## Code Analysis
### Inputs
- `n` (integer): The number of numbers to be entered.
___
### Flow
1. Initialize the variables `largest` and `smallest` to negative infinity and positive infinity respectively.
2. Iterate `n` times.
3. Prompt the user to enter a number.
4. Check if the entered number is larger than the current `largest` number. If so, update `largest` with the entered number.
5. Check if the entered number is smaller than the current `smallest` number. If so, update `smallest` with the entered number.
6. Print the largest and smallest numbers.
___
### Outputs
- The largest number among the entered numbers.
- The smallest number among the entered numbers.
___
