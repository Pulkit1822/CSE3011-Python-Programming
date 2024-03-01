for i in range(1, 501):
    num = i
    sum_of_cubes = 0
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    if sum_of_cubes == i:
        print(i)
