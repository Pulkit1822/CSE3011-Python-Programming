class Account:
    def __init__(self, number, balance, holder):
        self.number = number
        self.balance = balance
        self.holder = holder

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account {self.number} balance: {self.balance}")


def create_account():
    number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    holder = input("Enter account holder's name: ")
    return Account(number, balance, holder)


def main():
    accounts = []
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account = create_account()
            accounts.append(account)
            print("Account created successfully.")

        elif choice == "2":
            number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            for account in accounts:
                if account.number == number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")

        elif choice == "3":
            number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            for account in accounts:
                if account.number == number:
                    account.withdraw(amount)
                    break
            else:
                print("Account not found.")

        elif choice == "4":
            number = input("Enter account number: ")
            for account in accounts:
                if account.number == number:
                    account.check_balance()
                    break
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()