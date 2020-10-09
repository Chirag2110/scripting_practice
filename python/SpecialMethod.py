#!/usr/bin/env python3

import math

class SimpleProperty(object):
    def __init__(self, fget, fset):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, cls):
        return self.fget(instance)

    def __set__(self,instance, value):
        return self.fset(instance, value)


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi*self.radius**2

    def setArea(self):
        self.radius = math.sqrt(area/math.pi)
    area = SimpleProperty(getArea, setArea)

