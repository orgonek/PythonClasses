""" 
Dany jest plik sesjaEgzaminacyjna.csv, w którym dane zapisane s¡ w nast¦puj¡cy
sposób:
• 30 Jan 2021 : Programowanie w Assembler
• 02 Feb 2021 : Algorytmika i zao»ono±¢ obliczeniowa
• 04 Feb 2021 : Klaskanie rytmiczne
Sprawdzaj¡c dzisiejsz¡ dat¦ nale»y ustali¢, ile egzaminów zostaao jeszcze do ko«ca
sesji. Przykaadowo dla daty 1 stycznia 2021 wynikiem b¦dzie 3, ale dla daty 1 lutego
2021  2.
 """

import csv
from datetime import datetime

with open("sesja.txt", ) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter = ':')
   dict = {rows[0]:rows[1] for rows in csv_reader}


today = datetime.today()

exams = 0
for key in dict.keys():
    date = datetime.strptime(key.rstrip(),'%d %b %Y')
    if date > today:
        exams+=1

print(exams)

