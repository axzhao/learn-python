#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""

    >>> from import_demo import *
    >>> globals()['_not_be_import_var']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: '_not_be_import_var'

    >>> import import_demo
    >>> import_demo.__dict__['_not_be_import_var']
    '1'
    
"""

_not_be_import_var = '1'
import_var = '11'


def _notBeImportDef():
    print("2")


def importDef():
    print("22")


class _NotBeImportClass:
    pass


class ImportClass:
    pass
