
my_dict = {}

print("Enter element to add: ")
key = input()
value = int(input("Enter value: "))

my_dict[key] = value

print("Dictionary: ", my_dict)

print("Enter element to delete: ")
item_to_delete = input()

if item_to_delete in my_dict:
    del my_dict[item_to_delete]
else:
    print("Item not found in the dictionary")

print("Dictionary: ", my_dict)

print("Enter item to access: ")
item_to_access = input()

if item_to_access in my_dict:
    print(f"Value of {item_to_access} is {my_dict[item_to_access]}")
else:
    print("Item not found in the dictionary")

