def split_dict_of_lists_to_list_of_dicts(dict_of_lists):
    list_of_dicts = []
    for i in range(len(dict_of_lists[list(dict_of_lists.keys())[0]])):
        temp_dict = {}
        for key, value in dict_of_lists.items():
            temp_dict[key] = value[i]
        list_of_dicts.append(temp_dict)
    return list_of_dicts

dict_of_lists = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(split_dict_of_lists_to_list_of_dicts(dict_of_lists))



