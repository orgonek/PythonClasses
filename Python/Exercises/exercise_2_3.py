""" Do zadania doa¡czony zostaa plik csv z rzeczywistymi notowaniami spóaki indekso-
wanej na gieadzie. Plik skaada si¦ z daty oraz zmiany procentowej w cenie instru-
mentu wzgl¦dem poprzedniego odczytu. Bardzo cz¦sto w zestawieniach nansowych

przedstawia si¦ zwroty za ostatni miesi¡c. Nale»y odczyta¢ dane, nast¦pnie wyzna-
czy¢ ±redni¡ dla ka»dego z miesi¡ca i zapisa¢ ±rednie zmiany miesi¦czne w osobnym

pliku. """


import pandas as pd


data = pd.read_csv('1.csv',sep = ':', header = None)
data.columns = ['Date','Percentage change']
data['Date'] = data['Date'].str.slice_replace(4,7)
grouped = data.groupby(['Date']).mean().round(2)
grouped.to_csv('summary.csv',sep = ':')
