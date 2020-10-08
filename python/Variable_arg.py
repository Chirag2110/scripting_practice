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


def inclusive_range(*args):
    nargs = len(args)
    starts = 0
    step = 1

    # initialize parameters
    if nargs < 1:
        raise TabError(f'expected at least 1 argument, got {nargs}')
    elif nargs == 1:
        stop = args[0]
    elif nargs == 2:
        (starts, stop) = args
    elif nargs == 3:
        (starts, stop, step) = args
    else:
        raise TabError(f'expected at most 3 arguments, got {nargs}')

    # generator
    i = starts
    while i <= stop:
        yield i
        i += step


def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after function call')
    return f2


@f1
def f3():
    print('thi is f3')


def main():
    """
    y = ['meow', 'grrr', 'purr']
    x = dict(Buffy='meow', Zilla='grrr', Angel='purr')
    kitten(*y)
    kitten_dic(**x)
    """

    for i in inclusive_range(25):
        print(i, end=' ')
    print()
    # decorator to check the behaviour comment out line 52
    f3()



if __name__ == '__main__':
    main()
