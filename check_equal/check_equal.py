def check_equal(list1):
    return list1[1:] == list1[:-1]

x = [10, 20, 30, 40, 50]
y = [10, 20, 20, 20, 20]
z = [10, 10, 10, 10, 10]

print("x:", x)
print("y:", y)
print("z:", z)

print("check_equal(x):", check_equal(x))
print("check_equal(y):", check_equal(y))
print("check_equal(z):", check_equal(z))
