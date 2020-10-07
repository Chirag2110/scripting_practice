#!/usr/bin/env python3
from decimal import *

x = "seven {} {}".format(8, 9)
print(x)
print(type(x))

x = "seven {1} {0}".format(8, 9)
print(x)
print(type(x))

print(x.capitalize())
print(x.upper())
print(x.lower())

x = "seven {} {}".format(8, 9)

a = Decimal('0.1')
b = Decimal('0.3')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
