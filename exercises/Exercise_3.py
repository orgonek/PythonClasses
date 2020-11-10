""" Napisz funkcj¦ wypisuj¡c¡ co drugi element listy w odwrotnej kolejno±ci. Mo»na
u»y¢ metod wbudowanych dla list. """

def display_second(arr):
    list.reverse()

    for i in range(len(arr)):
        if i%2 == 0:
            print(list[i],end= ' ')


list = [1,2,3,4,5,6,7,8,9,10,11,12,['adam','ania']]

display_second(list)