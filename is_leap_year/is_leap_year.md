## Summary
This function checks if a given year is a leap year.

## Example Usage
```python
is_leap_year(2000)
# Output: True

is_leap_year(1900)
# Output: False
```

## Code Analysis
### Inputs
- year: an integer representing the year to be checked
___
### Flow
1. Check if the year is divisible by 400. If it is, return True.
2. If the year is not divisible by 400, check if it is not divisible by 100 and divisible by 4. If it is, return True.
3. If none of the above conditions are met, return False.
___
### Outputs
- True if the year is a leap year
- False if the year is not a leap year
___
