#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleClass():
    """
    >>> class rec: pass
    ... 
    >>> pers1 = rec()
    >>> pers1.name = 'mel'
    >>> pers2 = rec()
    >>> pers2.name = 'haha'
    >>> print(pers1.name, pers2.name)
    mel haha
    """


class Super:
    # default behavior
    def method(self):
        print("in Super.method")
    # expected to be defined
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!'

# inherit method verbatim
class Inheritor(Super):
    pass

class Replacer(Super):
    # replace method completely
    def method(self):
        print("in Replacer.method")


class Extender(Super):
    # extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Exterder.method')

class Provider(Super):
    # fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

print('\n')
print('Provider...')
x = Provider()
x.delegate()

class Sub(Super): pass

y =Sub()
y.delegate()