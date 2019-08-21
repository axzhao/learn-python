#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    x = General()
    raise x


def raiser1():
    x = Specific1()
    raise x


def raiser2():
    x = Specific2()
    raise x


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as x:
        import sys
        print('caught:', sys.exc_info()[0], x.__class__)


class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam.txt')


try:
    parser()
except FormatError as exc:
    exc.logerror()