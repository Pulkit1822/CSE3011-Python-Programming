def rotate_right(elements, k):
    n = len(elements)
    k = k % n
    return elements[n-k:] + elements[:n-k]


if __name__ == "__main__":
    # taking input from the user
    data = input("Enter list of integers separated by comma: ")
    list_of_integers = [int(i) for i in data.split(",")]
    k = int(input("Enter number of elements to be rotated by: "))

    # calling the function to rotate elements
    rotated_list = rotate_right(list_of_integers, k)

    # printing the rotated list
    print(f"Rotated list: {rotated_list}")