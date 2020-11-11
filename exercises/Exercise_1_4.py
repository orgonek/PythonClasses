""" Dane s¡ dwie listy. Napisz metod¦ Merge, która poa¡czy listy tak, »eby elementy
pojawiaay si¦ na zmian¦. """
l1 = [1,2,3,4,5,6]
l2 = ['a','b','c']

def merge(l1,l2):
    i = 0
    l3 = []
    while(i < len(l1) or i < len(l2)):
        if(i < len(l1)):
            l3.append(l1[i])
        if(i < len(l2)):
            l3.append(l2[i])
        i+=1
    return l3
    

print(merge(l1,l2))

       