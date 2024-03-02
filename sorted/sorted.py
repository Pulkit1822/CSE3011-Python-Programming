def isSorted(myList):
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            return False
    return True

n = int(input("Enter number of elements: "))
myList = []
print("Enter", n, "elements")
for i in range(n):
    ele = int(input())
    myList.append(ele)

if isSorted(myList):
    print("List is sorted")
else:
    print("List is not sorted")
