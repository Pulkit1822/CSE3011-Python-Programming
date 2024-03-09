## Summary
This code snippet determines whether a given year is a leap year or not.

## Example Usage
```python
Enter a year: 2020
2020 is a leap year.
```

## Code Analysis
### Inputs
- `year` (integer): The year to be checked.
___
### Flow
1. Prompt the user to enter a year.
2. Read the input and convert it to an integer.
3. Check if the year is divisible by 400 using the modulo operator (%).
4. If it is divisible by 400, or if it is not divisible by 100 but divisible by 4, then it is a leap year.
5. Print the appropriate message indicating whether the year is a leap year or not.
___
### Outputs
- If the year is a leap year, print "{year} is a leap year."
- If the year is not a leap year, print "{year} is not a leap year."
___
