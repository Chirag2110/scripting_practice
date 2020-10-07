#!/usr/bin/env python3

# set is an un-ordered data structure
t = "savaliya"
t = set(t)
print(t)

name = "chirag"
s = set(name)
t.update(s)
"""
a = t | s  Union of t and s
b = t & s  Intersection of t and s
c = t – s  Set difference (items in t, but not in s)
d = t ^ s  Symmetric difference (items in t or s, but not both)
"""
print(t | s)
print( t & s)
print ( t - s)
print( t ^ s)
