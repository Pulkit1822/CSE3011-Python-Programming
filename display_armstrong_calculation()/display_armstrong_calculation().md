### Code Snippet: Armstrong Numbers Finder

#### Inputs
The code snippet doesn't take any direct input from the user.

#### Flow
1. The code snippet iterates through numbers from 1 to 500 (inclusive).
2. For each number, it calculates the sum of cubes of its digits.
3. If the sum of cubes of digits is equal to the original number, it prints that number.

#### Outputs
The code snippet outputs Armstrong numbers found within the range of 1 to 500 (inclusive).

```python
def find_armstrong_numbers():
    for i in range(1, 501):
        num = i
        sum_of_cubes = 0
        while num > 0:
            digit = num % 10
            sum_of_cubes += digit ** 3
            num //= 10
        if sum_of_cubes == i:
            print(i)

find_armstrong_numbers()
