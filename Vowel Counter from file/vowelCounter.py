f = open("employees.txt", "r")
contents = f.read()
vowels = 'aeiouAEIOU'
count = 0
for letter in contents:
    if letter in vowels:
        count += 1
print("Number of vowels: ", count)
