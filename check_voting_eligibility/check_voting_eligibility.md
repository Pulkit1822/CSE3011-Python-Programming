## Summary
The `main` function prompts the user to enter their age, checks if they are eligible to vote using the `check_voting_eligibility` function, and prints a corresponding message.

## Example Usage
```python
Enter your age: 20
You have the right to vote.
```

## Code Analysis
### Inputs
- `age` (integer): the age of the user
___
### Flow
1. Prompt the user to enter their age.
2. Convert the input to an integer and assign it to the variable `age`.
3. Call the `check_voting_eligibility` function with the `age` as an argument.
4. If the return value is `True`, print "You have the right to vote."
5. If the return value is `False`, print "You do not have the right to vote."
___
### Outputs
- None
___
