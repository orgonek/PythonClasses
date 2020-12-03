""" Wygeneruj losow¡ list¦ o wielko±ci zadanej przez u»ytkownika. Lista mo»e zawiera¢
aa«cuchy, zmienne typu oat, int oraz warto±ci boolowskie. Nast¦pnie napisz metod¦,
która przyjmuje tak¡ list¦ jako parametr i dzieli j¡ na 4 nowe listy zawieraj¡ce osobno
elementy string, oat, int oraz boolean. """

import random
import string

def generate_value(value):
    if value == 0:
        return random.choice(string.ascii_letters)
    elif value == 1:
        return random.uniform(0,100)
    elif value == 2:
        return random.randint(0,100)
    else:
        return bool(random.choice(['True','False']))

def generate_list(n):
    list = []
    for i in range(n):
        list.append(generate_value(random.randint(0,3)))
    return list

def extract_list(list):
    str_list, flo_list,int_list,bool_list = [],[],[],[]
    for item in list:
        if isinstance(item,str):
            str_list.append(item)
        elif isinstance(item,float):
            flo_list.append(item)
        elif isinstance(item,bool):
            bool_list.append(item)
        else:
            int_list.append(item)
    return str_list,flo_list,int_list,bool_list



n = int(input('Enter number of elements '))
l = generate_list(n)
print(l)
extract_list(l)
