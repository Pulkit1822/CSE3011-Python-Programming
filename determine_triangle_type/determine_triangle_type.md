## Summary
This code defines a function called `determine_triangle_type` that takes three arguments representing the lengths of the sides of a triangle. The function determines the type of the triangle (equilateral, isosceles, or scalene) based on the lengths of the sides and prints the result.

## Example Usage
```python
determine_triangle_type(5, 5, 5)
# Output: Equilateral triangle

determine_triangle_type(5, 5, 6)
# Output: Isosceles triangle

determine_triangle_type(3, 4, 5)
# Output: Scalene triangle
```

## Code Analysis
### Inputs
- `side1`: an integer representing the length of the first side of the triangle.
- `side2`: an integer representing the length of the second side of the triangle.
- `side3`: an integer representing the length of the third side of the triangle.
___
### Flow
1. Check if all sides are equal (`side1 == side2 == side3`). If true, print "Equilateral triangle".
2. If the above condition is false, check if any two sides are equal (`side1 == side2` or `side2 == side3` or `side1 == side3`). If true, print "Isosceles triangle".
3. If both conditions above are false, print "Scalene triangle".
___
### Outputs
- The function does not return any value. It prints the type of the triangle based on the lengths of its sides.
___
