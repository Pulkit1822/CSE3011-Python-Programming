def check_voting_eligibility(age):
    return age >= 18

def main():
    age = int(input("Enter your age: "))
    if check_voting_eligibility(age):
        print("You have the right to vote.")
    else:
        print("You do not have the right to vote.")

if __name__ == "__main__":
    main()
