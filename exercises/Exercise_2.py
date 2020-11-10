""" Wygeneruj losow¡ list¦ o wielko±ci zadanej przez u»ytkownika. Lista mo»e zawiera¢
aa«cuchy, zmienne typu oat, int oraz warto±ci boolowskie. Nast¦pnie napisz metod¦,
która przyjmuje tak¡ list¦ jako parametr i dzieli j¡ na 4 nowe listy zawieraj¡ce osobno
elementy string, oat, int oraz boolean. """

import random
import string 

def generate_value(x):
    if x == 0:
        return random.choice(string.ascii_letters)
    elif x == 1:
        return random.uniform(0,100)
    elif x == 2:
        return random.randint(0,100)
    else:
        return bool(random.choice(['True','False']))

def generate_list(n):
    list = []
    for i in range(n):
        list.append(generate_value(random.randint(0,3)))
    return list

def extract_list(list):
    strList, floList,intList,boolList = [],[],[],[]
    for x in list:
        if isinstance(x,str):
            strList.append(x)
        elif isinstance(x,float):
            floList.append(x)
        elif isinstance(x,bool):
            boolList.append(x)
        else:
            intList.append(x)
    return strList,floList,intList,boolList 



n = int(input('Enter number of elements '))
list = generate_list(n)
print(list)
extract_list(list)