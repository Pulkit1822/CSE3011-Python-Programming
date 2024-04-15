def main():
    star_count = int(input("How many starred pyramids do you want: "))
    for row in range(star_count):
        for col in range(star_count - row - 1):
            print(" ", end="")
        for col in range(row + 1):
            print("* ", end="")
        print()

if __name__ == "__main__":
    main()
