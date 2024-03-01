### Code Snippet: Largest and Smallest Number Finder

#### Inputs
The code snippet takes input from the user in the form of integer numbers. The user can enter numbers until they want to stop by entering 0.

#### Flow
1. The code snippet initializes variables to keep track of the largest and smallest numbers entered.
2. It enters a while loop that continues until the user enters 0.
3. Inside the loop, it prompts the user to enter a number.
4. If the entered number is 0, the loop breaks.
5. Otherwise, it compares the entered number with the current largest and smallest numbers and updates them accordingly.
6. After the loop ends, it prints the smallest and largest numbers entered by the user.

#### Outputs
The code snippet outputs the smallest and largest numbers entered by the user.

```python
largest = None
smallest = None

while True:
    num = int(input("Enter a number (To stop press 0): "))
    if num == 0:
        break

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print(f"Smallest number entered is {smallest}")
print(f"Largest number entered is {largest}")
