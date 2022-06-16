from math import nan

from numpy import NaN


x = NaN
print(type(x))

if type(x) == type(1.1):
    print('float')
else:
    print('nofloat')
