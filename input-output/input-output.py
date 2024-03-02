user_input = input("Enter integers separated by spaces: ")

input_strings = user_input.split()

for string in input_strings:
    try:
        integer = int(string)
        print(integer)
    except ValueError:
        print(f"'{string}' is not an integer.")
