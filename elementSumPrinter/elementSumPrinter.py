number_of_elements = int(input("Enter number of elements: "))
elements_list = []

for _ in range(number_of_elements):
    element = int(input("Enter an element: "))
    elements_list.append(element)
    
total_sum = 0
for item in elements_list:
    total_sum += item
    
print("Sum of all elements:", total_sum)