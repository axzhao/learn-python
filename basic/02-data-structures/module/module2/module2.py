#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

print("starting to load...")
import sys
name = 42

def func():
    global name
    name = 99

class Klass:pass

print("done loading.")

print(__name__) # 导入者名称
print(__file__) # 那个文件加载的

def exampleModule2():
    """
    >>> import module2
    starting to load...
    done loading.
    module2
    /Users/Dev/vscode_python/02-def-module/module/module2/module2.py
    >>> module2.sys
    <module 'sys' (built-in)>
    >>> module2.func
    <function func at 0x109db2b70>
    >>> module2.Klass
    <class 'module2.Klass'>
    >>> list(module2.__dict__.keys())
    ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'sys', 'name', 'func', 'Klass', 'exampleModule2']
    >>> name = 88
    >>> import module2
    >>> module2.func()
    >>> print(name, module2.name)
    88 99
    """