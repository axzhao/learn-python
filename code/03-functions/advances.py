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


class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        print("fetch...")
        return instance._name

    def __set__(self, instance, value):
        print("change...")
        instance._name = value

    def __delete(self, instance):
        print("remove...")
        del instance._name


class Person3:
    def __init__(self, name):
        self._name = name

    name = Name()  # assign descriptor to attr


bob = Person3("Bob Smith")
print(bob.name)
bob.name = 'Rober Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person3('Sue Jones')
print(sue.name)
print(Name.__doc__)


class Person4:
    def __init__(self, name):
        self._name = name

    class Name:  # Using a nested class
        "name descriptor docs"

        def __get__(self, instance, owner):
            print("fetch...")
            return instance._name

        def __set__(self, instance, value):
            print("change...")
            instance._name = value

        def __delete(self, instance):
            print("remove...")
            del instance._name

    name = Name()


bob = Person4("Bob Smith")
print(bob.name)
bob.name = 'Rober Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person4('Sue Jones')
print(sue.name)
print(Person4.Name.__doc__)


class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("DescState get")
        return self.value * 10

    def __set__(self, instance, value):
        print("DescState set")
        self.value = value


class CalcAttrs:
    X = DescState(2)
    Y = 3

    def __init__(self):
        self.Z = 4


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)


class InstState:
    def __get__(self, instance, owner):
        print("InstState get")
        return instance._Y * 100

    def __set__(self, instance, value):
        print("InstState set")
        instance._Y = value


class CalcAttrs2:
    X = DescState(2)  # 描述符
    Y = InstState()  # 实例状态

    def __init__(self):
        self._Y = 3
        self.Z = 4


obj = CalcAttrs2()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)


class Person5:
    def __init__(self, name):
        self._name = name  # triggers setattr

    def __getattr__(self, attr):
        if attr == 'name':
            print('fetch...')
            return self._name  # does not loop: real attr
        else:
            raise AttributeError(attr)

    # # replace getattr with this
    # def __getattribute__(self, attr):
    #     if attr == 'name':
    #         print('fetch...')
    #         attr = '_name'
    #     return object.__getattribute__(self, attr)
    # # 每次获取属性都运行了两次，关心速度可以直接
    # def __getattribute__(self, attr):
    #     if attr == 'name':
    #       return object.__getattribute__(self, 'name') ** 2

    def __setattr__(self, attr, value):
        if attr == 'name':
            print('change...')
            attr = '_name'
        self.__dict__[attr] = value  # avoid looping here

    def __delattr__(self, attr):
        if attr == 'name':
            print('remove...')
            attr = '_name'  # avoid looping here too
        del self.__dict__[attr]


bob = Person5('Bob')
print(bob.name)
bob.name = 'Robert'
print(bob.name)
del bob.name
print('_' * 20)
sue = Person5('Sue')
print(sue.name)


# attr1 类属性
# attr2 实例属性
# attr3 虚拟的管理属性
class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    # 拦截未定义的
    def __getattr__(self, attr):
        print('get: ' + attr)
        return 3


x = GetAttr()
print(x.attr1)
print(x.attr2)
print(x.attr3)
print('_' * 40)


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    # 拦截所有的属性，并且必须将那些没有管理的属性访问指向超类获取器避免循环
    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


x = GetAttr()
print(x.attr1)
print(x.attr2)
print(x.attr3)
