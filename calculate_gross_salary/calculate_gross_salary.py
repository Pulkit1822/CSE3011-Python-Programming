def calculate_gross_salary(basic_salary):
    if basic_salary <= 10000:
        hra = basic_salary * 0.2
        da = basic_salary * 0.8
    elif basic_salary <= 20000:
        hra = basic_salary * 0.25
        da = basic_salary * 0.9
    else:
        hra = basic_salary * 0.3
        da = basic_salary * 0.95

    net_salary = basic_salary + hra + da
    ppf_deduction = net_salary * 0.1
    gross_salary = net_salary - ppf_deduction

    print(f"Basic Salary : {basic_salary:.2f}\nDA : {da:.2f}\nHRA : {hra:.2f}")
    print("-----------------------------------------")
    print(f"Net salary : {net_salary:.2f}\nPPF : -{ppf_deduction:.2f}")
    print("-----------------------------------------")
    print(f"Gross Salary : {gross_salary:.2f}")

if __name__ == "__main__":
    basic_salary = float(input("Basic salary: "))
    calculate_gross_salary(basic_salary)

