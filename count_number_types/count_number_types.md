### Code Snippet: Count Positive, Negative, and Zero Numbers

#### Inputs
The code snippet takes input from the user in the form of integer numbers.

#### Flow
1. The code snippet initializes three variables to keep track of the counts of positive, negative, and zero numbers.
2. It enters a while loop that continues until the user enters 0.
3. Inside the loop, it prompts the user to enter a number.
   - If the number is greater than 0, it increments the positive count variable.
   - If the number is less than 0, it increments the negative count variable.
   - If the number is equal to 0, it increments the zero count variable and breaks out of the loop.
4. After the loop ends, it prints the counts of positive, negative, and zero numbers entered by the user.

#### Outputs
The code snippet outputs the counts of positive, negative, and zero numbers entered by the user.

```python
def count_numbers():
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
            break

    print(f"Positive numbers entered: {positive_count}")
    print(f"Negative numbers entered: {negative_count}")
    print(f"Zeroes entered: {zero_count}")

count_numbers()
