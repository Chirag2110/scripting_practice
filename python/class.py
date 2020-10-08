#!/usr/bin/evn python3

class Duck:
    sound = 'Qauck, Qauck.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return  self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError(f'print_animal(): requires an Animal')
    else:
        print('The {} is named "{}" and says "{}" '.format(o.type(), o.name(), o.sound()))


def main():
    """
    donald = Duck()
    donald.quack()
    donald.move()
    """
    a0 = Animal('kitten', 'fluffy', 'rwar')
    print_animal(a0)


if __name__ == '__main__':
    main()
