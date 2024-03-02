list_data = input("Enter the list of numbers separated by space: ")
list_data = list_data.split()
list_data = [int(i) for i in list_data]

sub_list = input("Enter the sub list of numbers separated by space: ")
sub_list = sub_list.split()
sub_list = [int(i) for i in sub_list]

contains_sublist = False

for i in range(len(list_data)-len(sub_list)+1):
    if list_data[i:i+len(sub_list)] == sub_list:
        contains_sublist = True
        break

if contains_sublist:
    print("YES")
else:
    print("NO")