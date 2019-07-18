#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % self.calls, self.func, __name__)
        self.func(*args)


@tracer  # same as spam = tracer(spam)
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
