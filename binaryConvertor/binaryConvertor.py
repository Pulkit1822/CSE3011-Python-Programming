bin_num = input("Enter binary number: ")
dec_num = 0

# Using for loop
for i in range(len(bin_num)):
    dec_num += int(bin_num[-(i+1)])*(2**i)

print("Decimal number is:", dec_num)
