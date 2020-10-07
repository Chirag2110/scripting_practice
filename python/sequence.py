#!/usr/bin/env python3

"""
   Simple data structure in python
   list, dictionary and tuple
   list and dictionary are mutable while
   tuple is an immutable type data structure.
"""

x = [1, 2, 3, 4, 5]
for i in x:
    print("i is {}".format(i))

y = list(range(1, 10, 2))
for i in y:
    print("y is {}".format(y))
print(type(y))

z = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k, v in z.items():
    print("key = {} and value = {}".format(k, v))
print(type(z))


