## Summary
The `check_character_type` function checks the type of a given character and prints a corresponding message.

## Example Usage
```python
check_character_type('A')
```
Output: "The character 'A' is an alphabet."

## Code Analysis
### Inputs
- `char` (string): The character to be checked.
___
### Flow
1. Check if the character is an alphabet using the `isalpha()` method.
2. If it is an alphabet, print a message stating that.
3. If not, check if the character is a digit using the `isdigit()` method.
4. If it is a digit, print a message stating that.
5. If neither an alphabet nor a digit, print a message stating that the character is a special symbol.
___
### Outputs
- None
___
