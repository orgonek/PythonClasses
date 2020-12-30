""" Napisz waasn¡ metod¦ sort() umo»liwiaj¡c¡ sortowanie listy tak»e w sytuacji, kiedy
na li±cie znajduj¡ si¦ liczby i aa«cuchy. Zakaadamy, »e wszystkie elementy liczbowe
znajduj¡ si¦ na pocz¡tku, a aa«cuchy znajduj¡ si¦ w dalszej cz¦±ci listy - posortowane
saownikowo. """

def custom_sort(custom_list):
    string_list = [x for x in custom_list if isinstance(x, str)]
    number_list = [x for x in custom_list if isinstance(x, int)]

    string_list.sort()
    number_list.sort()

    return number_list+string_list

list_sample = ["ab",2,"aa",51,3,'ba',213,199,'cad','bu']
print(custom_sort(list_sample))
