""" Napisz waasn¡ metod¦ sort() umo»liwiaj¡c¡ sortowanie listy tak»e w sytuacji, kiedy
na li±cie znajduj¡ si¦ liczby i aa«cuchy. Zakaadamy, »e wszystkie elementy liczbowe
znajduj¡ si¦ na pocz¡tku, a aa«cuchy znajduj¡ si¦ w dalszej cz¦±ci listy - posortowane
saownikowo. """

def custom_sort(list):
    stringList = [x for x in list if isinstance(x, str)]
    numberList = [x for x in list if isinstance(x, int)]

    stringList.sort()
    numberList.sort()

    return numberList+stringList

list = ["ab",2,"aa",51,3,'ba',213,199,'cad','bu']
print(custom_sort(list))