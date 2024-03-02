number_of_elements = int(input("Enter number of elements: "))
unique_elements_list = []

for _ in range(number_of_elements):
    element = int(input("Enter an element: "))
    if element not in unique_elements_list:
        unique_elements_list.append(element)
        
if len(unique_elements_list) == number_of_elements:
    print("All elements are unique")
else:
    print("Not all elements are unique")

