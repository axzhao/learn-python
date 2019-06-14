#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    # type 异常类型
    # value 异常类实例
    # traceback 堆栈
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False


with TraceBlock() as action:
    action.message('test 1')
    print('reached')

with TraceBlock() as action:
    action.message('test 1')
    raise TypeError
    print('not reached')