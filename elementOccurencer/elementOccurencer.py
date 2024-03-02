input_elements = input("Enter the list elements separated by space: ")

elements_list = list(map(int, input_elements.split()))

element_count = {}

for element in elements_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

for element, count in element_count.items():
    print(f"{element} occurs {count} {'time' if count == 1 else 'times'}")