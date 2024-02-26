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
