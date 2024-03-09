## Summary
This code snippet determines the type of triangle based on the lengths of its sides.

## Example Usage
```python
Enter the 1st side: 5
Enter the 2nd side: 5
Enter the 3rd side: 5
Equilateral triangle
```

## Code Analysis
### Inputs
- `side1`: an integer representing the length of the first side of the triangle.
- `side2`: an integer representing the length of the second side of the triangle.
- `side3`: an integer representing the length of the third side of the triangle.
___
### Flow
1. Prompt the user to enter the lengths of the three sides of the triangle.
2. Check if all three sides are equal. If they are, print "Equilateral triangle".
3. If the sides are not all equal, check if any two sides are equal. If they are, print "Isosceles triangle".
4. If none of the sides are equal, print "Scalene triangle".
___
### Outputs
- "Equilateral triangle": if all three sides are equal.
- "Isosceles triangle": if any two sides are equal.
- "Scalene triangle": if none of the sides are equal.
___
