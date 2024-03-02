myList = list(map(int, input("Enter the list elements: ").split()))

mySet = set(myList)

if len(mySet) == len(myList):
    print("No, list does not contain duplicate element")
else:
    print("Yes, list contains duplicate element")
