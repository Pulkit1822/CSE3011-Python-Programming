char = input("Enter a single character: ")
if len(char) == 1:
    if char.isalpha():
        print(f"The character '{char}' is an alphabet.")
    elif char.isdigit():
        print(f"The character '{char}' is a digit.")
    else:
        print(f"The character '{char}' is a special symbol.")
else:
    print("Please enter a single character.")