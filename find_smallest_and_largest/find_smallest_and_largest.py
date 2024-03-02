def find_smallest_and_largest(n):
    largest = float('-inf')
    smallest = float('inf')
    
    for _ in range(n):
        num = int(input("Enter a number: "))
        
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")

if __name__ == "__main__":
    n = int(input("Enter the total numbers: "))
    find_smallest_and_largest(n)