""" Przy pomocy biblioteki random wygeneruj tablic¦ o rozmiarze podanym przez 
uzytkownika. Tablica powinna zawiera¢ tylko zmienne typu oat. Nastepnie wyznacz srednia tablicy korzystajac z metody
wbudowanej, a nastepnie te sama srednia bezmetod wbudowanych. Wyznacz tez mediane listy (skorzystaj z metody sort, ale nie
uzywaj funkcji dotyczacej wyznaczania mediany). """

import random
from statistics import mean, median


def generate_arr(size):
    arr = []
    for i in range(size): 
        arr.append(random.uniform(0,100))
    return arr

def my_mean(arr):
    sum = 0.0
    count = 0

    for i in (arr):
        sum+=i
        count+=1
    
    return sum/count

def my_median(arr):
    arr.sort()
    n = len(arr)
    condition = n %2 == 0
    if condition:
        i = int(n/2)
        return (arr[i-1] + arr[i])/2
    return arr[(n//2)]

num = int(input("Enter a number: "))
genArr = generate_arr(num)
print(genArr)
print('Genarated list {} \nMean function {} \nMy mean function {} \n'.format(genArr,mean(genArr),my_mean(genArr)))
print('Median', my_median(genArr))
print(median(genArr))