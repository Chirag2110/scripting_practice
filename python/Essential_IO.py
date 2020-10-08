#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Please supply a filename")
    raise SystemExit

f = open(sys.argv[1])
values = f.readlines()
f.close()

f_values = [float(s) for s in values]

print("Minimum of f_values {}".format(min(f_values)))
print("Maximum of f_values {}".format(max(f_values)))
