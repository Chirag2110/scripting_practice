#!/usr/bin/env python3
import  sys
try:
    f = open('main_.py')
    for line in f:
        print(line)
except IOError:
    e = "could not open file main_.py"
    print(e)
