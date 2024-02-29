def check_prime_number():
    num = int(input("Enter a positive integer: "))
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

check_prime_number()
