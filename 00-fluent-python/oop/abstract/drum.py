#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from random import shuffle

from tombola import Tombola


class TumblingDrum(Tombola):

    def __init__(self, iterable):
        self._balls = []
        self.load(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)
        shuffle(self._balls)

    def pick(self):
        return self._balls.pop()
