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


def compare_others(_a):
    if type(_a) is list:
        print("{} is of {}".format(_a, type(_a)))
    # if isinstance(_a, file):
    #    print("{} is of {}".format(_a, type(_a)))


def main():
    a_list = [a, b]
    compare(a, b)
    compare_others(a_list)
    compare_others('chapter2.py')


if __name__ == '__main__':
    main()
