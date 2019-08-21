#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import b
x = 1

def exampleReload():
    """
    >>> import a
    >>> a.x, a.b.y, a.b.c.z
    (1, 2, 3)

    # change z = 8

    >>> from importlib import reload
    >>> reload(a)
    <module 'a' from '/Users/Dev/vscode_python/02-def-module/reload/a.py'>
    >>> a.x, a.b.y, a.b.c.z
    (1, 2, 3)
    >>> from reloadall import reload_all
    >>> reload_all(a)
    reloading: a
    reloading: b
    reloading: c
    >>> a.x, a.b.y, a.b.c.z
    (1, 2, 8)
    """