## Summary
This code defines a function named `calculate_gross_salary` that calculates the gross salary based on the given basic salary. It takes the basic salary as input and calculates the house rent allowance (HRA), dearness allowance (DA), net salary, provident fund (PPF) deduction, and gross salary. The function then prints the calculated values.

## Example Usage
```python
calculate_gross_salary(15000)
```
This will calculate the gross salary for a basic salary of 15000 and print the breakdown of the salary components.

## Code Analysis
### Inputs
- `basic_salary` (numeric): The basic salary of an employee.
___
### Flow
1. The function checks if the `basic_salary` is less than or equal to 10000. If true, it calculates the HRA as 20% of the `basic_salary` and the DA as 80% of the `basic_salary`.
2. If the `basic_salary` is greater than 10000 but less than or equal to 20000, it calculates the HRA as 25% of the `basic_salary` and the DA as 90% of the `basic_salary`.
3. If the `basic_salary` is greater than 20000, it calculates the HRA as 30% of the `basic_salary` and the DA as 95% of the `basic_salary`.
4. The function then calculates the net salary by adding the `basic_salary`, HRA, and DA.
5. It calculates the PPF deduction as 10% of the net salary.
6. Finally, it calculates the gross salary by subtracting the PPF deduction from the net salary.
___
### Outputs
- The function prints the breakdown of the salary components, including the basic salary, DA, HRA, net salary, PPF deduction, and gross salary.
___

## Purpose
The purpose of this code snippet is to demonstrate how to calculate the gross salary of an employee based on their basic salary. It allows the user to input the basic salary and then calculates and prints the various components of the salary, including the house rent allowance (HRA), dearness allowance (DA), net salary, provident fund (PPF) deduction, and gross salary. This is a practical example of how to work with conditionals and arithmetic operations in Python.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `calculate_gross_salary.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python calculate_gross_salary.py
   ```
5. Follow the prompt to enter the basic salary. The breakdown of the salary components, including the gross salary, will be printed as the output.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter the basic salary. For example:
```python
Basic salary: 15000
Basic Salary : 15000.00
DA           : 13500.00
HRA          : 3750.00
-----------------------------------------
Net salary   : 32250.00
PPF          : -3225.00
-----------------------------------------
Gross Salary : 29025.00
```
In this example, the user enters the basic salary as `15000`. The breakdown of the salary components, including the gross salary `29025.00`, is printed as the output.
