def calculate_char_frequency(s):
    s_dict = dict()
    for i in s.lower():
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    return s_dict


print(calculate_char_frequency("veni vedi vici"))
