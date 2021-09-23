def combine_dicts(*args:dict):
    res = dict()
    for d in args:
        for k, v in d.items():
            if k in res:
                res[k] += v
            else: res[k] = v
    return res


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))