""" Dane s¡ dwie listy. Napisz metod¦ Merge, która poa¡czy listy tak, »eby elementy
pojawiaay si¦ na zmian¦. """


def merge(list_1,list_2):
    i = 0
    list_3 = []
    while i < len(list_1) or i < len(list_2):
        if i < len(list_1):
            list_3.append(list_1[i])
        if i < len(list_2):
            list_3.append(list_2[i])
        i+=1
    return list_3

l1 = [1,2,3,4,5,6]
l2 = ['a','b','c']
print(merge(l1,l2))
       