class FormulaError(Exception):
    pass

def calculate():
    try:
        user_input = input("Enter a number, an operator (+ or -), and another number (separated by spaces): ")
        inputs = user_input.split()

        if len(inputs) != 3:
            raise FormulaError("Invalid input. Input must consist of 3 elements.")

        num1 = float(inputs[0])
        operator = inputs[1]
        num2 = float(inputs[2])

        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Operator must be '+' or '-'.")

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)

    except ValueError:
        raise FormulaError("Invalid input. Numbers must be valid.")

    except FormulaError as e:
        print("FormulaError:", e)

calculate()