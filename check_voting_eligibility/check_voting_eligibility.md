## Summary
This code snippet is a simple program that checks if a person is eligible to vote based on their age.

## Example Usage
```python
Enter age: 25
You are eligible to vote.
```

## Code Analysis
### Inputs
- `age` (integer): The age of the person.
___
### Flow
1. Prompt the user to enter their age.
2. Convert the input to an integer and assign it to the variable `age`.
3. Check if `age` is greater than or equal to 18 and less than or equal to 100.
4. If the condition is true, print "You are eligible to vote."
5. If the condition is false, print "You are not eligible to vote."
___
### Outputs
- "You are eligible to vote." if the age is between 18 and 100 (inclusive).
- "You are not eligible to vote." if the age is less than 18 or greater than 100.
___

## Purpose
The purpose of this code snippet is to demonstrate how to check if a person is eligible to vote based on their age in Python. It allows the user to input their age and then determines whether they are eligible to vote. This is a fundamental operation in Python programming and is useful for understanding how to work with conditionals and user input.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `check_voting_eligibility.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python check_voting_eligibility.py
   ```
5. Follow the prompt to enter your age. The code will determine if you are eligible to vote and print the result.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter your age. For example:
```python
Enter age: 25
You are eligible to vote.
```
In this example, the user enters the age `25`. The code determines that the user is eligible to vote and prints the corresponding message.
