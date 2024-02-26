## Summary
This function checks if a given list of binary numbers is divisible by 5.

## Example Usage
```python
binary_numbers = "101,110,111,1001"
result = check_binary_divisibility(binary_numbers)
print(result)
```

## Code Analysis
### Inputs
- `bin_numbers`: a string containing a comma-separated list of binary numbers.
___
### Flow
1. Split the `bin_numbers` string into individual binary numbers using the comma as a delimiter.
2. Iterate over each binary number.
3. Convert each binary number to its decimal equivalent using `int(num, 2)`.
4. Check if the decimal number is divisible by 5 using the modulo operator `%`.
5. If the number is divisible by 5, add it to the `divisible_by_5` list.
6. Join the numbers in the `divisible_by_5` list with commas using `','.join(divisible_by_5)`.
7. Return the resulting string.
___
### Outputs
- A string containing the binary numbers from the input list that are divisible by 5.
___
