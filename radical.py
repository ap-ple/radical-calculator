from math import sqrt
from stuff import *

while True:
    clear()
    print('Square Root Calculator')
    x = num_input('Enter number: √')
    if type(x) == str:
        input(x)
    elif sqrt(x) != int(sqrt(x)):
        print('Simplest Radical Form:')
        print(radical(x))
        print('Decimal:')
        input(f'~{sqrt(x)}')
    else:
        input(f'Square Root: {int(sqrt(x))}')
