def sum_of_numbers_and_palindrome():
    num = int(input("Enter a number: "))
    total_sum = sum(range(num + 1))
    
    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
    
    return total_sum

sum_of_numbers_and_palindrome()
