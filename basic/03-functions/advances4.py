#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)

    def remainGet(self):
        return self.retireage - self.age

    remain = property(remainGet)


bob = CardHolder('1234-5678', 'Bob', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep='/')
bob.name = 'Bob Q'
bob.age = 50
bob.acct = '23-45-67-89'
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep='/')

sue = CardHolder('5678-12-34', 'Sue', 35, '124 main st')
print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep='/')
try:
    sue.age = 200
except:
    print('Bad age for sue')

try:
    sue.remain = 5
except:
    print('Cannot set sue.remain')

try:
    sue.acct = '1234567'
except:
    print('Bad acct for sue')


class CardHolder2:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr


class Name:
    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        value = value.lower().replace(' ', '_')
        self.__name = value


name = Name()


class Age:
    def __get__(self, instance, owner):
        return self.age

    def __set__(self, instance, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.age = value


age = Age()


class Acct:
    def __get__(self, instance, owner):
        return self.acct[:3] + '***'

    def __set__(self, instance, value):
        value = value.replace('-', '')
        if len(value) != instance.acctlen:
            raise TypeError('invald acct number')
        else:
            self.acct = value


acct = Acct()


class Remain:
    def __get__(self, instance, owner):
        return instance.retireage - instance.age

    def __set__(self, instance, value):
        raise TypeError('cannot set remain')


remain = Remain()


class CardHolder3:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, name):
        if name == 'acct':
            return self._acct[:3] + '***'
        elif name == 'ramain':
            return self.retireage - self.age
        else:
            raise AttributeError(name)

    def __setattr__(self, name, vlaue):

        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':

            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')

        self.__dict__[name] = value



class CardHolder4:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattribute__(self, name):
        superget = object.__getattribute__
        if name == 'acct':
            return superget.(self, 'acct')[:3] + '***'
        elif name == 'ramain':
            return superget.(self, 'retireage') - superget.(self, 'age')
        else:
            raise superget.(self, name)

    def __setattr__(self, name, vlaue):

        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'age':

            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')

        self.__dict__[name] = value
