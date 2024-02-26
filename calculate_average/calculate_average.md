## Summary
This code defines a function named `calculate_average` that calculates the average of a given number of students' marks.

## Example Usage
```python
average = calculate_average(3)
print(average)
```
This code will prompt the user to enter the marks of 3 students, calculate their average, and then print the result.

## Code Analysis
### Inputs
- `num_students`: an integer representing the number of students for which the average needs to be calculated.
___
### Flow
1. Initialize `total_marks` variable to 0.
2. Iterate `num_students` times:
   - Prompt the user to enter a student's mark.
   - Add the entered mark to `total_marks`.
3. Calculate the average by dividing `total_marks` by `num_students`.
4. Return the calculated average.
___
### Outputs
- `average`: a float representing the average of the students' marks.
___
