""" Napisz funkcj¦ zliczaj¡c¡ liczb¦ znaków w pliku. """

import collections
from string import ascii_letters, ascii_lowercase


def count_characters(name):
    with open(name,encoding='UTF-8') as text_file:
        data = text_file.read()

    count = len(data)
    print(f'All characters including spaces {count}')

def count_letters(filename, case_sensitive = False):
    with open(filename,'r', encoding='UTF-8',) as file:
        data = file.read()

    if case_sensitive:
        alphabet = ascii_letters
    else:
        alphabet = ascii_lowercase
        data = data.lower()

    letter_count = collections.Counter(char for char in data if char in alphabet)

    return letter_count


count_characters('sampleText.txt')
print(count_letters('sampleText.txt'))
