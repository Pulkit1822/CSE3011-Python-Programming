# Get input from the user
user_input = input("Enter integers separated by spaces: ")

# Split the input string into individual string integers
input_strings = user_input.split()

# Convert string integers to integers and print each one
for string in input_strings:
    try:
        integer = int(string)
        print(integer)
    except ValueError:
        print(f"'{string}' is not an integer.")
