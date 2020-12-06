"""
U»ytkownik proszony jest o podanie formatu danych u»ywaj¡c liter y, m oraz d.
Przykaadowe formaty to: yyyy.mm.dd, yyyy/mm/dd, dd:mm:yyyy, dd:mm:yy (gdzie
yy to dwie ostatnie cyfry roku) i tak dalej. Nale»y napisa¢ funkcj¦, która konwertuje
dat¦ z biblioteki timedate na format podany przez u»ytkownika. Przykaadowo:
• 10 Jan 2021 -> 2021.01.10 (dla formatu yyyy.mm.dd);
• 05 Feb 2021 -> 05:02:2021 (dla formatu dd:mm:yyyy).
"""


from datetime import datetime
import re


def convert_date(custom_format, date):

    variables = re.split('([^a-zA-Z])',custom_format)
    values = {
        'dd':'d',
        'mm':'m',
        'yy':'y',
        'yyyy':'Y',
    }

    data_string = ''

    for value in variables:
        if value in values:
            data_string += f'%{values.get(value)}'
        else:
            data_string += value

    return date.strftime(data_string)

my_date = datetime.now()
user_format = input('Enter your format using letters m,d,y for example (dd:mm:yyyy) ')
print(convert_date(user_format,my_date))
