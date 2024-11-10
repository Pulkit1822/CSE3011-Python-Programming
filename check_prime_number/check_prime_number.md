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

## Purpose
The purpose of this code snippet is to demonstrate how to check if a given positive integer is a prime number in Python. It allows the user to input a positive integer and then determines whether the number is a prime number or not. This is a fundamental operation in Python programming and is useful for understanding how to work with loops and conditionals.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `check_prime_number.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python check_prime_number.py
   ```
5. Follow the prompt to enter a positive integer. The code will determine if the entered number is a prime number and print the result.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter a positive integer. For example:
```python
Enter a positive integer: 7
7 is a prime number.
```
In this example, the user enters the positive integer `7`. The code determines that `7` is a prime number and prints the corresponding message.
