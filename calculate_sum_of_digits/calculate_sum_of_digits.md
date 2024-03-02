## Summary
This code snippet takes a list of numbers as input from the user, converts the list elements to integers, calculates the sum of digits for each number in the list, and then prints the list of digit sums.

## Example Usage
```python
Enter the list of numbers separated by comma: 123, 45, 678
[6, 9, 21]
```

## Code Analysis
### Inputs
- A list of numbers separated by commas.
___
### Flow
1. Prompt the user to enter a list of numbers separated by commas.
2. Split the input string by commas to get a list of number strings.
3. Convert each number string to an integer using a list comprehension.
4. Initialize an empty list to store the sum of digits for each number.
5. Iterate over the list of integers.
6. For each number, initialize a variable `sum_of_digits` to 0.
7. Use a while loop to calculate the sum of digits for the current number.
8. Inside the while loop, get the last digit of the number using the modulo operator and add it to `sum_of_digits`.
9. Divide the number by 10 to remove the last digit.
10. Repeat steps 8 and 9 until the number becomes 0.
11. Append the final `sum_of_digits` to the `digit_sums` list.
12. Print the `digit_sums` list.
___
### Outputs
- A list of integers representing the sum of digits for each number in the input list.
___
