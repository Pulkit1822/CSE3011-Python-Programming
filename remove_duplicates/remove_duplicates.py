
# getting the input from the user
data = input("Enter the list elements separated by space: ")

# converting the string to list
list_data = data.split()

# converting the list to integers
list_data = [int(i) for i in list_data]

# creating a set to remove the duplicates
unique_set = set(list_data)

# converting the set back to list
distinct_list = list(unique_set)

# printing the list
print(distinct_list)



