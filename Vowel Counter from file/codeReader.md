## Summary
This code snippet reads the contents of a file named "employees.txt" and counts the number of vowels in the file.

## Example Usage
```python
# employees.txt file contains the following text:
# John Doe
# Jane Smith
# Alex Johnson

f = open("employees.txt", "r")
contents = f.read()
vowels = 'aeiouAEIOU'
count = 0
for letter in contents:
    if letter in vowels:
        count += 1
print("Number of vowels: ", count)
```

## Code Analysis
### Inputs
- The code snippet requires a file named "employees.txt" to be present in the same directory.
- The file should contain text.
___
### Flow
1. The code snippet opens the file "employees.txt" in read mode.
2. It reads the entire contents of the file and stores it in the variable `contents`.
3. It initializes a variable `vowels` with all the vowels in lowercase and uppercase.
4. It initializes a variable `count` to keep track of the number of vowels.
5. It iterates over each character in the `contents` string.
6. If the character is a vowel (present in the `vowels` string), it increments the `count` variable.
7. Finally, it prints the total number of vowels found in the file.
___
### Outputs
- The code snippet outputs the total number of vowels found in the file.
___
