""" 
Przeprowadzi¢ dyskretyzacj¦ atrybutów w taki sposób, »e wszystkie warto±ci poni-
»ej 0.5 zamienione zostan¡ na warto±¢ 0, a wszystkie powy»ej 0.5  na warto±¢ 1.
Narysowa¢ histogram dla dowolnego atrybutu po dyskretyzacji.

"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('abalone.csv')
data = data.drop(columns=['M'])
data.columns = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

data = data.mask(data < 0.5, 0)
data = data.mask(data > 0.5, 1)

plt.hist(data['Whole weight'],)
plt.show()