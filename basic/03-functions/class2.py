#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from abc import ABCMeta, abstractclassmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractclassmethod
    def action(self):
        pass


# error
# x = Super()


class Sub(Super):
    def action(self):
        print('spam')


x = Sub()
x.delegate()