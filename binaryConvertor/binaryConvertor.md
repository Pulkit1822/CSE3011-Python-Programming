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
```

## Purpose
The purpose of this code snippet is to demonstrate how to convert a binary number to its decimal equivalent in Python. It allows the user to input a binary number and then calculates and prints the corresponding decimal number. This is a fundamental operation in computer science and is useful for understanding how binary and decimal number systems work.

## Instructions to Run the Code
1. Ensure that Python is installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/)
2. Copy the code snippet into a Python file, for example, `binaryConvertor.py`.
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the Python file using the following command:
   ```bash
   python binaryConvertor.py
   ```
5. Follow the prompt to enter a binary number. The decimal equivalent of the binary number will be printed as the output.

## Example Usage and Expected Output
When you run the code, you will be prompted to enter a binary number. For example:
```python
Enter binary number: 1010
Decimal number is: 10
```
In this example, the user enters the binary number `1010`. The decimal equivalent `10` is printed as the output.
