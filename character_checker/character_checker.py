def check_character_type(char):
    if char.isalpha():
        print(f"The character '{char}' is an alphabet.")
    elif char.isdigit():
        print(f"The character '{char}' is a digit.")
    else:
        print(f"The character '{char}' is a special symbol.")

if __name__ == "__main__":
    user_input = input("Enter a single character: ")
    if len(user_input) == 1:
        check_character_type(user_input)
    else:
        print("Please enter a single character.")
