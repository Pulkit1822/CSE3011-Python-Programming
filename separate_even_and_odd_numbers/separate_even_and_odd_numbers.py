L=[int(x) for x in input("Enter elements separated by space: ").split()]

even_numbers=list()
odd_numbers=list()

for i in L:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")

