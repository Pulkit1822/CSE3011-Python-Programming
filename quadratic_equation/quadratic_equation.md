## Summary
The `find_roots` function calculates the roots of a quadratic equation using the quadratic formula. It determines whether the roots are real or complex based on the discriminant value.

## Example Usage
```python
roots = find_roots(1, -3, 2)
print(roots)
```

## Code Analysis
### Inputs
- `a`: the coefficient of the quadratic term
- `b`: the coefficient of the linear term
- `c`: the constant term
___
### Flow
1. Calculate the discriminant using the formula `b**2 - 4*a*c`.
2. If the discriminant is greater than 0, there are two distinct real roots. Calculate the roots using the quadratic formula: `(-b + sqrt(discriminant)) / (2*a)` and `(-b - sqrt(discriminant)) / (2*a)`.
3. If the discriminant is equal to 0, there is one real root. Calculate the root using the formula `-b / (2*a)`.
4. If the discriminant is less than 0, there are complex roots. Calculate the real and imaginary parts of the roots using the formulas `-b / (2*a)` and `sqrt(-discriminant) / (2*a)`, respectively.
___
### Outputs
- If the discriminant is greater than 0, the function returns a tuple containing the two distinct real roots.
- If the discriminant is equal to 0, the function returns a tuple containing the single real root.
- If the discriminant is less than 0, the function returns a tuple containing the complex roots in the form of `(real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)`.
___
