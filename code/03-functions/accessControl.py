#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        # if not __debug__:
        #     return aClass
        # else:
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance_wrapped':
                    self.__dict__[attr] = value  # avoid looping
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)

        return onInstance

    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


def exampleXxx():
    """
    """