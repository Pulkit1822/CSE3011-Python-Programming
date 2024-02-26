## Summary
This function calculates the electricity bill based on the number of units consumed.

## Example Usage
```python
bill = calculate_electricity_bill(100)
print(bill)
```
Output:
```
82.5
```

## Code Analysis
### Inputs
- units: an integer representing the number of units consumed
___
### Flow
1. Check if the number of units is less than or equal to 50. If true, calculate the bill by multiplying the units by 0.50.
2. If the number of units is greater than 50, check if it is less than or equal to 150. If true, calculate the bill by adding the cost of the first 50 units (50 * 0.50) to the cost of the remaining units ((units - 50) * 0.75).
3. If the number of units is greater than 150, check if it is less than or equal to 250. If true, calculate the bill by adding the cost of the first 50 units (50 * 0.50), the cost of the next 100 units (100 * 0.75), and the cost of the remaining units ((units - 150) * 1.20).
4. If the number of units is greater than 250, calculate the bill by adding the cost of the first 50 units (50 * 0.50), the cost of the next 100 units (100 * 0.75), the cost of the next 100 units (100 * 1.20), and the cost of the remaining units ((units - 250) * 1.50).
5. Calculate the surcharge by multiplying the bill by 0.20.
6. Calculate the total bill by adding the bill and the surcharge.
___
### Outputs
- total_bill: a float representing the total electricity bill, including the surcharge.
___
