L = list(map(int, input("Enter the list of numbers separated by space: ").split()))
N = int(input("Enter the number of consecutive numbers: "))

# list to store the numbers that are repeated N times consecutively
consecutive_numbers = []

# loop through the list to find the consecutive numbers
for i in range(len(L)-N+1):
    count = 1
    for j in range(i+1, i+N):
        if L[j] != L[j-1]:
            break
        count += 1
    if count == N and L[i] not in consecutive_numbers:
        consecutive_numbers.append(L[i])

# print the result
if consecutive_numbers:
    print("YES")
    print(consecutive_numbers)
else:
    print("NO")