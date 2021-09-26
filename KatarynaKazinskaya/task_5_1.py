file = open("data/unsorted_names.txt", 'r')
names = file.readlines()
names.sort()
file2 = open("sorted_names.txt", 'w')
for i in names:
    file2.write(i)
file.close()
file2.close()
