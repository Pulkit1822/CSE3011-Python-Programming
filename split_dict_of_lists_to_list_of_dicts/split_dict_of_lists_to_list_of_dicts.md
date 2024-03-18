## Summary
This code snippet is a function called `split_dict_of_lists_to_list_of_dicts` that takes a dictionary of lists as input and returns a list of dictionaries. Each dictionary in the output list represents a combination of values from the input lists.

## Example Usage
```python
dict_of_lists = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(split_dict_of_lists_to_list_of_dicts(dict_of_lists))
```

## Code Analysis
### Inputs
The input to the `split_dict_of_lists_to_list_of_dicts` function is a dictionary where the keys are strings and the values are lists of equal length. Each key represents a category and each list represents the values for that category.
___
### Flow
1. Initialize an empty list called `list_of_dicts`.
2. Iterate over the range of the length of any of the input lists (assuming they all have the same length).
3. For each iteration, create an empty dictionary called `temp_dict`.
4. Iterate over the key-value pairs in the input dictionary.
5. For each key-value pair, assign the value at the current index to the corresponding key in `temp_dict`.
6. Append `temp_dict` to `list_of_dicts`.
7. Return `list_of_dicts`.
___
### Outputs
The output of the `split_dict_of_lists_to_list_of_dicts` function is a list of dictionaries. Each dictionary in the output list represents a combination of values from the input lists. The keys in each dictionary correspond to the keys in the input dictionary, and the values are the values at the same index from the input lists.
___
