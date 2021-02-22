""" 
Dla danych abalone wyznaczy¢ ±rednie i mediany dla ka»dego z atrybutów typu float.
"""

import numpy as np
import pandas as pd

data = pd.read_csv('abalone.csv')
data = data.drop(columns=['M'])
data.columns = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

for column in data.columns:
    if data.dtypes[column] != 'float64':
        data = data.drop(columns=[column])

mean_columns = data.mean(axis=0)
median_columns = data.median(axis=0)


print(f'Columns median\n{median_columns}')
print(f'Columns mean\n{mean_columns}')

print(data.describe())
