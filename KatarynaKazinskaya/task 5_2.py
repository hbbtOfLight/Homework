import string


def most_common_words(filepath, count=3):
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    frequency = dict()
    unique_words = list()

    for s in data.split():
        s = s.strip(string.digits + string.punctuation + string.whitespace).lower()
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1
            unique_words.append(s.lower())
    unique_words.sort(key=lambda x: frequency[x], reverse=True)
    return unique_words[:count]


print(most_common_words("data/lorem_ipsum.txt", 3))
print(most_common_words("data/lorem_ipsum.txt", 2))
