import string


def erase_repeats(s: str):
    s = s.lower()
    for i, ch in enumerate(s):
        s = s[0:i + 1] + s[i + 1:].replace(ch, "")
    return s


class Cipher:
    old_alphabet = string.ascii_lowercase

    def __init__(self, keyword: string):
        keyword = erase_repeats(keyword)
        self.alphabet = string.ascii_lowercase
        for i in self.alphabet:
            if i in keyword:
                self.alphabet = self.alphabet.replace(i, '')
        self.alphabet = keyword + self.alphabet

    def encode(self, word):
        new_word = ''
        for i in word:
            if i.isalpha():
                idx = ord(i.lower()) - ord('a')
                if i.isupper():
                    new_word += self.alphabet[idx].upper()
                else:
                    new_word += self.alphabet[idx]
            else:
                new_word += i
        return new_word

    def decode(self, word):
        new_word = ''
        for i in word:
            if i.isalpha():
                idx = self.alphabet.find(i.lower())
                if i.isupper():
                    new_word += self.old_alphabet[idx].upper()
                else:
                    new_word += self.old_alphabet[idx]
            else:
                new_word += i
        return new_word


cipher = Cipher("crypto")
cipher1 = Cipher("aaa")
print(cipher1.encode("Hello world"))
print(cipher1.decode("Hello world"))
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
