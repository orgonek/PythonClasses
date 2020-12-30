""" Napisz funkcj¦ wypisuj¡c¡ co drugi element listy w odwrotnej kolejno±ci. Mo»na
u»y¢ metod wbudowanych dla list. """

def display_second(arr):
    arr.reverse()

    for count,item in enumerate(arr):
        if count%2 == 0:
            print(arr[count],end= ' ')


l = [1,2,3,4,5,6,7,8,9,10,11,12,['adam','ania']]

display_second(l)
