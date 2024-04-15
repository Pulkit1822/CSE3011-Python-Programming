def main():
    row_count = int(input("Enter row count: "))
    for row in range(row_count):
        for col in range(row + 1):
            print("* ", end="")
        print()

if __name__ == "__main__":
    main()
