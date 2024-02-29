# Initialize counts for positive, negative, and zeros
positive_count = 0
negative_count = 0
zero_count = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
    
    if num == 0:
        break

print("Positive numbers entered:", positive_count)
print("Negative numbers entered:", negative_count)
print("Zeroes entered:", zero_count)
