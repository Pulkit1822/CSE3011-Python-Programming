def find_largest_of_four(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        return num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        return num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        return num3
    else:
        return num4

if __name__ == "__main__":
    numbers = input("Enter four numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    largest = find_largest_of_four(*numbers)
    print(f"The largest number is: {largest}")
