def calculate_electricity_bill(units):
    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = (50 * 0.50) + ((units - 50) * 0.75)
    elif units <= 250:
        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    else:
        bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
    
    surcharge = bill * 0.20
    total_bill = bill + surcharge
    
    return total_bill

if __name__ == "__main__":
    units = float(input("Enter the number of units consumed: "))
    total = calculate_electricity_bill(units)
    print(f"The total electricity bill is: Rs. {total:.2f}")
