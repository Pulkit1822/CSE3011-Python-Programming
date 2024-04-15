def test_index(data, index):
    try:
        result = data[index]
        print("Result:", result)
    except IndexError:
        print("Error: Index out of range.")

nums = [1, 2, 3, 4, 5, 6, 7]
index = int(input("Input the index: "))
test_index(nums, index)
