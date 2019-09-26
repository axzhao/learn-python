#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import inspect


def get_current_function_name():
    print('5', sys._getframe().f_code.co_name)
    return inspect.stack()[1][3]


class MyClass:
    def function_one(self):
        print('3', inspect.stack()[0][3])
        print('4', sys._getframe().f_code.co_name)
        print("6 %s.%s invoked" %
              (self.__class__.__name__, get_current_function_name()))


if __name__ == '__main__':
    print('1', sys._getframe().f_code.co_name)
    print('2', inspect.stack()[0][3])
    myclass = MyClass()
    myclass.function_one()

    print(sys._getframe().f_code)
    print(inspect.stack())
