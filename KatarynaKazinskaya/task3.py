def unique_sorted(s):
    s_list = s.split(',')
    appear_count = dict((k, 0) for k in s_list)
    for i, v in enumerate(s_list):
        appear_count[v] += 1
    s_list.clear()
    for k, v in appear_count.items():
        if v == 1:
            s_list.append(k)
    s_list.sort()
    return s_list


print(unique_sorted("aba,oba,biba,boba,pupa,lupa,pupa,lupa,biba"))