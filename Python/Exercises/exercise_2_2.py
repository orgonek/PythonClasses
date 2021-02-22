""" Dany jest plik, gdzie w ka»dej linii znajduje si¦ saowo. Nale»y sprawdzi¢, czy dane

saowo jest palindromem, a nast¦pnie do pliku csv zapisa¢ dla ka»dego saowa nast¦pu-
j¡ce dane: liczba porz¡dkowa, saowo, wypisa¢ wszystkie znaki znajduj¡ce si¦ w tym

saowie, wpisa¢ true  je»eli saowo jest palindromem i false, je»eli nie jest.
 """

import csv

def check_palindrome(word):
    return word == word[::-1]

with open('1.txt', 'r', encoding='UTF-8') as file:
    count = 1
    with open('1.csv', 'w', newline= '') as write_file:
        writer = csv.writer(write_file)
        for line  in file:
            line = line.strip()
            writer.writerow([count,line,''.join(set(line)),check_palindrome(line)])
            count+=1
