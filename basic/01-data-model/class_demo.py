#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class S:
    def __new__(cls):
        print('--- new ---', cls.__name__)
        return super().__new__(cls)

    def __init__(self):
        print('--- self ---', self.__class__.__name__)


class C(S):
    def __new__(cls):
        print('--- new ---', cls.__name__)
        return super().__new__(cls)  # 必须返回对象的引用，否则self找不到对象

    def __init__(self):
        print('--- self ---', self.__class__.__name__)
        super().__init__()


if __name__ == "__main__":
    C()
