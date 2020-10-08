#!/usr/bin/env python3

def kitten(*args):
    if len(args):
        for s in args:
            print(s, end=' ')
    else:
        print('meow.', end=' ')
    print('\n')


def kitten_dic(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('meow')


def main():
    kitten('meow', 'grrr', 'purr')
    kitten_dic(Buffy='meow', Zilla='grrr', Angel='purr')


if __name__ == '__main__':
    main()
