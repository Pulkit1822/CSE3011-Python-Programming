def print_pyramid(rows):
  for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
      print(" ", end="")
    for k in range(1, 2 * i):
      print(i, end="")
    print()


if __name__ == "__main__":
  print_pyramid(5)