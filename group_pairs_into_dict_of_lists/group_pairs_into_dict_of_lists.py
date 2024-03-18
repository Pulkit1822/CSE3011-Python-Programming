def group_pairs_into_dict_of_lists(pairs):
    result = {}
    for key, value in pairs:
        result.setdefault(key, []).append(value)
    return result

pairs = []

num_pairs = int(input("Enter the number of pairs: "))

for i in range(num_pairs):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    pairs.append((key, value))

print("Original list:")
print(pairs)

print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(group_pairs_into_dict_of_lists(pairs))
