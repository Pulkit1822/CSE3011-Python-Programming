### Code Snippet: Binary to Decimal Converter

#### Inputs
The code snippet takes input from the user in the form of a binary number.

#### Flow
1. The code snippet prompts the user to enter a binary number.
2. It initializes a variable to store the equivalent decimal number.
3. Using a for loop, it iterates through each digit of the binary number.
4. For each digit, it calculates its decimal equivalent and adds it to the total decimal number.
5. After the loop ends, it prints the decimal equivalent of the binary number.

#### Outputs
The code snippet outputs the decimal equivalent of the entered binary number.

```python
bin_num = input("Enter binary number: ")
dec_num = 0

# Using for loop
for i in range(len(bin_num)):
    dec_num += int(bin_num[-(i+1)])*(2**i)

print("Decimal number is:", dec_num)
