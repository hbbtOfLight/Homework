def replace(s):
    s2 = str()
    for c in s:
        if c == '"':
            s2 += "'"
        elif c == "'":
            s2 += '"'
        else:
            s2 += c
    return s2


print(replace("n\'\"\'"))

