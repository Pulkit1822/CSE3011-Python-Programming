strings = input("Enter strings separated by space: ").split()
count = 0
for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(f"Number of strings with length 2 or more and first and last characters are the same: {count}")
