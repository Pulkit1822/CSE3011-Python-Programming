def check_vowel_or_consonant(letter):
    vowels = 'aeiou'
    if letter.lower() in vowels:
        print(f"'{letter}' is a vowel.")
    elif letter.isalpha():
        print(f"'{letter}' is a consonant.")
    else:
        print(f"'{letter}' is not a letter.")

if __name__ == "__main__":
    user_input = input("Enter a single letter: ")
    if len(user_input) == 1:
        check_vowel_or_consonant(user_input)
    else:
        print("Please enter a single letter.")
