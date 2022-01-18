class Format:
    def __init__(self, word):
        self.word = word
    def big(self):
        print ('>>>', self.word.upper())

word = str(input('Enter word >>> '))

rect = Format(word)
rect.big()