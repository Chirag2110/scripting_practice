#!/usr/bin/env python3


class Foo(object):
    def __init__(self):
        self.items = []

    def update(self, x):
        self.items.append(x)

    @classmethod
    def whatami(cls):
        return cls


def main():
    foo = Foo()
    foo.update(21)
    print(foo.items)
    print(Foo.whatami())


if '__name__' == '__main__':
    main()
