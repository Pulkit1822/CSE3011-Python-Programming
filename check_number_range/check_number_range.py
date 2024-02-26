def check_number_range(number):
    if number <= 20:
        print(f"{number} is less than or equal to 20.")
    elif number <= 40:
        print(f"{number} is less than or equal to 40.")
    elif number <= 60:
        print(f"{number} is less than or equal to 60.")
    else:
        print(f"{number} is greater than 60.")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    check_number_range(num)
