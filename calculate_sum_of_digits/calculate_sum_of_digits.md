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

## Purpose
The purpose of this code snippet is to demonstrate how to calculate the sum of digits for each number in a list of numbers in Python. It allows the user to input a list of numbers, and then calculates and prints the sum of digits for each number. This is a fundamental operation in Python programming and is useful for understanding how to work with loops and arithmetic operations.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `calculate_sum_of_digits.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python calculate_sum_of_digits.py
   ```
5. Follow the prompt to enter a list of numbers separated by commas. The sum of digits for each number in the list will be printed as the output.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter a list of numbers separated by commas. For example:
```python
Enter the list of numbers separated by comma: 123, 45, 678
[6, 9, 21]
```
In this example, the user enters the list of numbers `123`, `45`, and `678`. The sum of digits for each number `[6, 9, 21]` is printed as the output.
