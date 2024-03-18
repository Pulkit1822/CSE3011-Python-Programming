new_dict = {}

# Prompt the user for input
num_keys = int(input("Enter the number of keys: "))

# Iterate over the range of keys
for i in range(num_keys):
    key = int(input("Enter the key: "))
    value = int(input("Enter the value: "))
    new_dict[key] = value

print(new_dict)
