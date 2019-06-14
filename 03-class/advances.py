#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, "name property docs")


class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)


class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()


x = Subject()
x.attr  # Descriptor.__get__(Subject.attr, x, Subject)
Subject.attr

# 当描述符的实例参数为None时，该描述符将直接访问它。


class D:
    def __get__(*args):
        print('get')


class C:
    a = D()


x = C()
x.a
C.a
x.a = 99  # stored on x, hiding C.a
x.a
list(x.__dict__.keys())
y = C()
y.a
C.a
