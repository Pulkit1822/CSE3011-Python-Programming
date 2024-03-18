## Summary
This code snippet defines a function called `group_pairs_into_dict_of_lists` that takes a list of key-value pairs and groups them into a dictionary of lists based on the keys. It then prompts the user to enter the number of pairs and the key-value pairs, and prints the original list and the grouped dictionary.

## Example Usage
```python
Enter the number of pairs: 5
Enter the key: yellow
Enter the value: 1
Enter the key: blue 
Enter the value: 2
Enter the key: yellow
Enter the value: 3
Enter the key: blue
Enter the value: 4
Enter the key: red
Enter the value: 1
Original list:
[('yellow', '1'), ('blue', '2'), ('yellow', '3'), ('blue', '4'), ('red', '1')]

Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': ['1', '3'], 'blue': ['2', '4'], 'red': ['1']}
```

## Code Analysis
### Inputs
- `pairs`: A list of key-value pairs.
___
### Flow
1. The function `group_pairs_into_dict_of_lists` is defined.
2. The function initializes an empty dictionary called `result`.
3. The function iterates over each key-value pair in the `pairs` list.
4. For each pair, the function checks if the key already exists in the `result` dictionary. If not, it adds the key to the dictionary with an empty list as the value.
5. The function then appends the value to the list associated with the key in the `result` dictionary.
6. After iterating through all the pairs, the function returns the `result` dictionary.
7. The code prompts the user to enter the number of pairs.
8. The code then prompts the user to enter the key and value for each pair and appends them to the `pairs` list.
9. The code prints the original list of pairs.
10. The code calls the `group_pairs_into_dict_of_lists` function with the `pairs` list and prints the resulting grouped dictionary.
___
### Outputs
- The original list of key-value pairs.
- The grouped dictionary where the keys are unique and the values are lists of corresponding values.
___
