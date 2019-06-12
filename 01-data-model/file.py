#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exmapleFile():
    """
    >>> myfile = open('myfile.txt', 'w')
    >>> myfile.write("hello text file\n")
    16
    >>> myfile.write("goodbye text file\n")
    18
    >>> myfile.close()
    >>> myfile = open("myfile.txt")
    >>> myfile.readline()
    'hello text file\n'
    >>> myfile.readline()
    'goodbye text file\n'
    >>> myfile.readline()
    ''
    >>> open("myfile.txt").read()
    'hello text file\ngoodbye text file\n'
    >>> print(open("myfile.txt").read())
    hello text file
    goodbye text file

    >>> data = open('myfile.txt', 'rb').read()
    >>> data
    b'hello text file\ngoodbye text file\n'
    >>> data.rstrip()
    b'hello text file\ngoodbye text file'


    >>> f= open('datafile.txt', 'w')
    >>> f.write('Spam\n')
    5
    >>> f.write('%s,%s,%s\n'%(1,2,3))
    6
    >>> f.write(str([4,5,6])+'$'+str({'a':11,'b':22})+'\n')
    29
    >>> f.close()
    >>> chars = open('datafile.txt').read()
    >>> print(chars)
    Spam
    1,2,3
    [4, 5, 6]${'a': 11, 'b': 22}

    >>> f = open('datafile.txt')
    >>> line = f.readline()
    >>> line
    'Spam\n'
    >>> line.rstrip()
    'Spam'
    >>> line = f.readline()
    >>> line
    '1,2,3\n'
    >>> parts = line.split(',')
    >>> parts
    ['1', '2', '3\n']
    >>> int(parts[1])
    2
    >>> numbers = [int(p) for p in parts]
    >>> numbers
    [1, 2, 3]
    >>> line = f.readline()
    >>> line
    "[4, 5, 6]${'a': 11, 'b': 22}\n"
    >>> parts = line.split('$')
    >>> parts
    ['[4, 5, 6]', "{'a': 11, 'b': 22}\n"]
    >>> eval(parts[0])
    [4, 5, 6]
    >>> objects = [eval(p) for p in parts]
    >>> objects
    [[4, 5, 6], {'a': 11, 'b': 22}]

    # eval会执行python的任何表达式，甚至有可能会删除所有文件的表达式，pickle模块会是一个理想的选择
    >>> d = {'a':1,'b':2}
    >>> f = open('datafile.pkl', 'wb')
    >>> import pickle
    >>> pickle.dump(d,f)
    >>> f.close()
    >>> f = open('datafile.pkl', 'rb')
    >>> e = pickle.load(f)
    >>> e
    {'a': 1, 'b': 2}

    >>> with open(r'datafile.txt') as myfile:
    ...     for line in myfile:
    ...             print(line)
    ... 
    Spam

    1,2,3

    [4, 5, 6]${'a': 11, 'b': 22}

    """