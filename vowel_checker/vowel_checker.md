## Summary
This function checks whether a given letter is a vowel, consonant, or not a letter.

## Example Usage
```python
check_vowel_or_consonant('a')
```
Output: "'a' is a vowel."

## Code Analysis
### Inputs
- letter: a string representing a single letter.
___
### Flow
1. Create a string variable `vowels` containing all the vowel letters.
2. Convert the input letter to lowercase using the `lower()` method.
3. Check if the lowercase letter is in the `vowels` string.
4. If it is, print that the letter is a vowel.
5. If not, check if the letter is an alphabetic character using the `isalpha()` method.
6. If it is, print that the letter is a consonant.
7. If it is neither a vowel nor a consonant, print that it is not a letter.
___
### Outputs
- A message indicating whether the input letter is a vowel, consonant, or not a letter.
___
