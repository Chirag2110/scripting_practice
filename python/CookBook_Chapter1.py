#!/usr/bin/env python3

import sys
print("PYTHON Version : {}".format(sys.version))

# unpack N tuple or sequence to N variables

p = (4, 5)
x, y = p
print("x: {} y: {}".format(x, y))

data = ['ACMR', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name: {} shares:{} price: {} date: {} ".format(name, shares, price, date))
name, shares, price, (year, month, day) = data

# unpacking works with any object which is iterable
# like: list, string, tuple and dict etc

s = 'Hello'
a, b, c, d, e = s
print("a: {} b: {} c: {} d: {} e: {}".format(a, b, c, d, e))

# To discard certain value

# noinspection PyRedeclaration
_, shares, price, _ = data
print("shares:{} price: {} ".format(shares, price))


"""
   1.2 Unpacking Elements from arbitary length
"""

# use * operator

record = ('dave', 'dave@example.com', '773-555-1212', '847-555-1212')

_name, _email, *phone_numbers = record

print("phone_numbers {}".format(phone_numbers))


records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(x):
    print('bar', x)

for tags, *args in records:
    if tags == 'foo':
        do_foo(*args)
    elif tags == 'bar':
        do_bar(*args)
    else:
        print("tags: {} args: ".format(tags, *args))
