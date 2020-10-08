#!/usr/bin/env python3

a = 2
b = 2


def compare(_a, _b):
    print('id of _a is {}'.format(id(_a)))
    print('id of _b is {}'.format(id(_b)))
    if _a is _b:
        print("a is b")
    if _a == _b:
        print("a == b")
    if type(_a) is type(_b):
        print("type of a and b both are same !")


def main():
    compare(a, b)


if __name__ == '__main__':
    main()
