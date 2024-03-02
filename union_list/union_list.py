L1 = list(map(int, input("Enter first sorted list of elements separated by comma: ").split(',')))
L2 = list(map(int, input("Enter second sorted list of elements separated by comma: ").split(',')))

union_list = []

i = j = 0
while i < len(L1) and j < len(L2):
    if L1[i] < L2[j]:
        if L1[i] not in union_list:
            union_list.append(L1[i])
        i += 1
    elif L1[i] > L2[j]:
        if L2[j] not in union_list:
            union_list.append(L2[j])
        j += 1
    else:
        if L1[i] not in union_list:
            union_list.append(L1[i])
        i += 1
        j += 1

while i < len(L1):
    if L1[i] not in union_list:
        union_list.append(L1[i])
    i += 1

while j < len(L2):
    if L2[j] not in union_list:
        union_list.append(L2[j])
    j += 1

print("Union of the lists: ", union_list)