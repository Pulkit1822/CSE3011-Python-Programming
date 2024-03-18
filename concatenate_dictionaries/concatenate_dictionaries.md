## Summary
This code snippet prompts the user to enter the number of keys for a dictionary and then asks for the key-value pairs. It creates a dictionary with the entered key-value pairs and prints the resulting dictionary.

## Example Usage
```python
Enter the number of keys: 3
Enter the key: 1
Enter the value: 10
Enter the key: 2
Enter the value: 20
Enter the key: 3
Enter the value: 30
{1: 10, 2: 20, 3: 30}
```

## Code Analysis
### Inputs
- `num_keys`: an integer representing the number of keys for the dictionary
- `key`: an integer representing the key for each key-value pair
- `value`: an integer representing the value for each key-value pair
___
### Flow
1. The code prompts the user to enter the number of keys for the dictionary.
2. It then iterates over the range of keys.
3. For each key, it prompts the user to enter the key and value.
4. It adds the key-value pair to the `new_dict` dictionary.
5. Finally, it prints the resulting dictionary.
___
### Outputs
- `new_dict`: a dictionary containing the entered key-value pairs.
___
