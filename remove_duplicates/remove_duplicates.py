L = input("Enter list of elements separated by comma: ").split(",")
x = int(input("Enter element to be removed: "))

L = [int(i) for i in L]

result = [i for i in L if i != x]

print(result)

