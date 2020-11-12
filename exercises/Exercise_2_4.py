""" Dla pliku z poprzedniego zadania wy±wietl na ekranie dane tylko dla miesi¡ca i roku
podanego przez u»ytkownika. """



import pandas as pd


data = pd.read_csv('1.csv',sep = ':', header = None)
data.columns = ['Date','Percentage change']
data['Date'] = data['Date'].str.slice_replace(4,7)

month = input('Enter month ')
year = input('Enter year ')

user_choice = f'{month[:3]} {year}'
user_result = data.loc[data['Date'].str.rstrip() == user_choice].mean()

print(f'Stats in {month} {year} : {user_result}')
