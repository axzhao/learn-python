#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleFile1():
    """
    >>> open('temp', 'w').write('abc\n')
    4
    >>> open('temp', 'r').read()
    'abc\n'
    >>> open('temp', 'rb').read()
    b'abc\n'
    >>> 
    >>> open('temp', 'wb').write(b'a\x00c')
    3
    >>> open('temp', 'r').read()
    'a\x00c'
    >>> open('temp', 'rb').read()
    b'a\x00c'
    >>> 
    >>> 
    >>> ba = bytearray(b'\x01\x02\x03')
    >>> open('temp', 'wb').write(ba)
    3
    >>> open('temp', 'r').read()
    '\x01\x02\x03'
    >>> open('temp', 'rb').read()
    b'\x01\x02\x03'
    >>> 
    >>> 
    >>> open('temp', 'w').write('abc\n')
    4
    >>> open('temp', 'w').write(b'abc\n')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: write() argument must be str, not bytes
    >>> 
    >>> 
    >>> open('temp', 'wb').write(b'abc\n')
    4
    >>> open('temp', 'w').write(b'abc\n')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: write() argument must be str, not bytes
    >>> 
    >>> 
    >>> chr(0xFF)
    'ÿ'
    >>> chr(0xFE)
    'þ'
    >>> s = 'A\xc4B\xe8C'
    >>> open('latindata', 'w', encoding='latin-1').write(s)
    5
    >>> open('utf8data', 'w', encoding='utf-8').write(s)
    5
    >>> open('latindata', 'rb').read()
    b'A\xc4B\xe8C'
    >>> open('utf8data', 'rb').read()
    b'A\xc3\x84B\xc3\xa8C'
    >>> open('latindata', 'r', encoding='latin-1').read()
    'AÄBèC'
    >>> open('utf8data', 'r', encoding='utf-8').read()
    'AÄBèC'
    >>> 
    >>> x = open('latindata', 'rb').read()
    >>> x.decode('latin-1')
    'AÄBèC'
    >>> x = open('utf8data', 'rb').read()
    >>> x.decode()
    'AÄBèC'
    >>> 
    """

