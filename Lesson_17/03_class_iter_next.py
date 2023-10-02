from string import ascii_letters


class EnglishLetters:
    def __init__(self):
        self.pos = -1
        self.letters = list(ascii_letters)

    def __iter__(self):
        return self

    def __next__(self):
        self.pos += 1
        if self.pos == len(self.letters):
            raise StopIteration
        return self.letters[self.pos]


el_iter = EnglishLetters()
# print(next(el_iter))
# print(next(el_iter))
# print(next(el_iter))

#
# for itm in el_iter:
#     print(itm)

print(*[itm for itm in el_iter], sep=' ')
