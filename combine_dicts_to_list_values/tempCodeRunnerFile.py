def get_user_input():
    dict1 = {}
    dict2 = {}

    # Get user input for dict1
    dict1_input = input("Enter key-value pairs for dict1 (separated by commas): ")
    dict1_pairs = dict1_input.split(',')
    for pair in dict1_pairs:
        key, value = pair.split(':')
        dict1[key.strip()] = int(value.strip())

    # Get user input for dict2
    dict2_input = input("Enter key-value pairs for dict2 (separated by commas): ")
    dict2_pairs = dict2_input.split(',')
    for pair in dict2_pairs:
        key, value = pair.split(':')
        dict2[key.strip()] = int(value.strip())

    return dict1, dict2