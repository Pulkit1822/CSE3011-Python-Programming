def check_binary_divisibility(bin_numbers):
    divisible_by_5 = []
    for num in bin_numbers.split(','):
        if int(num, 2) % 5 == 0:
            divisible_by_5.append(num)
    return ','.join(divisible_by_5)

if __name__ == "__main__":
    input_numbers = input("Enter comma separated 4 digit binary numbers: ")
    result = check_binary_divisibility(input_numbers)
    print(result)
