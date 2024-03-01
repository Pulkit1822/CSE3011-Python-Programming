# Checking weather the list contains duplicate element or not

# taking input from the user
myList = list(map(int, input("Enter the list elements: ").split()))

# Creating a set from the list
mySet = set(myList)

# Checking the length of the set and list
if len(mySet) == len(myList):
    print("No, list does not contain duplicate element")
else:
    print("Yes, list contains duplicate element")
