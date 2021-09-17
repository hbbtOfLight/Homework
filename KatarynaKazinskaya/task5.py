def print_unique_dictionary_values(dict_list):
    unique_count = dict()
    for d in dict_list:
        for k, v in d.items():
            if v in unique_count:
                unique_count[v] += 1
            else:
                unique_count[v] = 1
    print(unique_count)
    unique_list = list()
    for k, v in unique_count.items():
        if v == 1:
            unique_list.append(k)
    print(unique_list)


print_unique_dictionary_values(
    [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}])
