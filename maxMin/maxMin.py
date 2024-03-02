def maxMin(myList):
    if len(myList) == 0:
        return None, None
    maximum = minimum = myList[0]
    for i in range(1, len(myList)):
        if myList[i] > maximum:
            maximum = myList[i]
        if myList[i] < minimum:
            minimum = myList[i]
    return maximum, minimum

list1 = input("Enter numbers separated by a space: ").split()
list1 = [int(item) for item in list1]

max1, min1 = maxMin(list1)
print("Maximum is", max1)
print("Minimum is", min1)