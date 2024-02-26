def find_smallest_and_largest(n):
    # Initialize variables to store the largest and smallest numbers
    largest = float('-inf')
    smallest = float('inf')
    
    for _ in range(n):
        num = int(input("Enter a number: "))
        
        # Check if the number is the largest or smallest so far
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")

if __name__ == "__main__":
    n = int(input("Enter the total numbers: "))
    find_smallest_and_largest(n)