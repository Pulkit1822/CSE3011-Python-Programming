## Summary
This function checks whether a given positive integer is a prime number or not.

## Example Usage
```python
Enter a positive integer: 7
7 is a prime number.
```

## Code Analysis
### Inputs
- `num`: a positive integer entered by the user.
___
### Flow
1. Prompt the user to enter a positive integer.
2. Check if the entered number is greater than 1.
3. If it is, iterate from 2 to the entered number (exclusive).
4. For each iteration, check if the entered number is divisible by the current iteration number.
5. If it is, print that the entered number is not a prime number and break out of the loop.
6. If the loop completes without finding any divisors, print that the entered number is a prime number.
7. If the entered number is not greater than 1, print that it is not a prime number.
___
### Outputs
- If the entered number is a prime number, print that it is a prime number.
- If the entered number is not a prime number, print that it is not a prime number.
___
