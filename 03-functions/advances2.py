#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


# 2 dynamically computed attributes with properties
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square**2

    def setSquare(self, value):
        self._square = value

    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube**3

    cube = property(getCube)


x = Powers(3, 4)
print(x.square)
print(x.cube)
x.square = 5
print(x.square)


# same, but with descriptors
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square**2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        return instance._cube**2


class Powers2:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square  # self.square = square works too because it triggers desc __set__
        self._cube = cube


# same, but with generic __getattr__ undefined attribute interception
class Powers3:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square**2
        elif name == 'cube':
            return self._cube**3
        else:
            raise TypeError('unkonwn attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


# same, but with generic __getattribute__ all attribute interception
class Powers4:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square')**2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube')**3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] == value
