L = input("Enter list of numbers separated by comma: ").split(",")
N = int(input("Enter Nth position from largest or smallest: "))

# Converting string to int
L = [int(i) for i in L]

# Finding Nth largest element
L.sort(reverse=True)
largest = L[N-1]
print(f"{N} largest is = {largest}")

# Finding Nth smallest element
L.sort()
smallest = L[N-1]
print(f"{N} smallest is={smallest}")
