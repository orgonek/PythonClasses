""" 
Dane abalone dost¦pne do tego ¢wiczenia wczyta¢ w programie, usun¡¢ z zestawu
danych wszystkie atrybuty inne ni» oat. Nast¦pnie posortowa¢ zestaw danych na
podstawie atrybutu wskazanego przez u»ytkownika.

"""

import pandas as pd

data = pd.read_csv('abalone.csv')
data = data.drop(columns=['M'])
data.columns = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

value = input('Enter name of the column by which you want to sort the data ')

if value in data.columns:
    data = data.sort_values(by=[value])
else:
    print('Enter correct column name')

print(data)