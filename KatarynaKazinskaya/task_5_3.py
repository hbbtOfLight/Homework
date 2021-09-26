def get_top_performers(file_path, number_of_top_students=5):
    file = open(file_path, 'r')
    data = file.readlines()
    student_names = list()
    marks = dict()
    for s in data[1:]:
        name = s.split(',')[0]
        mark = float(s.split(',')[-1])
        student_names.append(name)
        marks[name] = mark
    student_names.sort(key=lambda x:marks[x], reverse=True)
    return student_names[:number_of_top_students]


def print_info_to_file(filepath):
    file = open(filepath, 'r')
    data = file.readlines()
    ages = dict()
    for s in data:
        ages[s] = s.split(',')[1]
    data.sort(key=lambda x:ages[x], reverse=True)
    file.close()
    file2 = open("sorted_students.csv", 'w')
    for s in data:
        file2.write(s)





print(get_top_performers('data/students.csv'))
print_info_to_file('data/students.csv')
