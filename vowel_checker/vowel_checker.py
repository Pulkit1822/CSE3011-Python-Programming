letter = input("Enter a single letter: ")

if len(letter) == 1:
    vowels = 'aeiou'
    if letter.lower() in vowels:
        print(f"'{letter}' is a vowel.")
    elif letter.isalpha():
        print(f"'{letter}' is a consonant.")
    else:
        print(f"'{letter}' is not a letter.")