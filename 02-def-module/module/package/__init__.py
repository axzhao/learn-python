#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

bar = ''

print('dir1 init')
x = 1

def exmaple():
    """
    >>> import dir1.dir2.mod
    dir1 init
    dir2 init
    in mod.py
    >>> import dir1.dir2.mod
    >>> from importlib import reload
    >>> reload(dir1)
    dir1 init
    <module 'dir1' from '/Users/Dev/vscode_python/02-def-module/module/dir/dir1/__init__.py'>
    >>> reload(dir1.dir2)
    dir2 init
    <module 'dir1.dir2' from '/Users/Dev/vscode_python/02-def-module/module/dir/dir1/dir2/__init__.py'>
    >>> quit()

    >>> from dir1.dir2 import mod
    dir1 init
    dir2 init
    in mod.py
    >>> import dir1.dir2.mod as mod
    """