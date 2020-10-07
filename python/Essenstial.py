#!/usr/bin/env python3

import sys

f = open("sequence.py")
line = f.read()
while line:
    print(line)
    line = f.read()
f.close()

sys.stdout.write("Enter Your name :")
name = sys.stdin.readline()
print("Fuck You {}".format(name))

# short version of above code
name = raw_input("Enter Your name :")
