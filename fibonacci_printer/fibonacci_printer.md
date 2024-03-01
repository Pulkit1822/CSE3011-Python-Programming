### Code Snippet: Fibonacci Series Printer

#### Inputs
The code snippet takes input from the user specifying the number of terms in the Fibonacci series.

#### Flow
1. The code snippet initializes the first two terms of the Fibonacci series.
2. It enters a while loop that iterates until the desired number of terms are printed.
3. Within the loop, it prints the current term of the Fibonacci series.
4. It updates the values of the first two terms for the next iteration.
5. After printing all terms, it ends the program.

#### Outputs
The code snippet outputs the Fibonacci series up to the specified number of terms.

```python
def print_fibonacci_series():
    # take input from the user
    n = int(input("How many terms? "))

    # first two terms
    a = 0
    b = 1

    count = 0
    while count < n:
       print(a, end=' ')
       a, b = b, a + b
       count += 1

    # end the program
    print()

print_fibonacci_series()
