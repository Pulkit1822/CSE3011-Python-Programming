def combine_dicts_to_list_values(dict1, *dict_list):
    print("Original dictionaries:\n")
    for dictionary in [dict1, *dict_list]:
        print(dictionary)
    print("\nCombined dictionaries, creating a list of values for each key:")
    combined_dict = {}
    for dictionary in [dict1, *dict_list]:
        for key, value in dictionary.items():
            if key not in combined_dict:
                combined_dict[key] = [value]  # Create a new list for the key if it doesn't exist
            else:
                combined_dict[key].append(value)  # Append the value to the existing list for the key
    print(combined_dict)


if __name__ == "__main__":
    dict1 = {"w": 50, "x": 100, "y": "Green", "z": 400}
    dict2 = {"x": 300, "y": "Red", "z": 600}
    combine_dicts_to_list_values(dict1, dict2)

