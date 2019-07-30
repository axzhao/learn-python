#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import collections


# https://github.com/fluentpython/example-code/blob/master/03-dict-set/transformdict.py
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
