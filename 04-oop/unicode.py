#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def exampleUnicode():
    """
    >>> b = b'spam'
    >>> s = 'eggs'
    >>> type(b), type(s)
    (<class 'bytes'>, <class 'str'>)
    >>> b
    b'spam'
    >>> s
    'eggs'
    >>> b[0],s[0]
    (115, 'e')
    >>> b[1:],s[1:]
    (b'pam', 'ggs')
    >>> list(b),list(s)
    ([115, 112, 97, 109], ['e', 'g', 'g', 's'])

    >>> b[0] = 'x'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'bytes' object does not support item assignment
    >>> s[0] = 'x'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    >>> b = b"""
    ... xxx
    ... yyy
    ... """
    >>> b
    b'\nxxx\nyyy\n'
    
    >>> s = 'eggs'
    >>> s.encode()
    b'eggs'
    >>> bytes(s, encoding='ascii')
    b'eggs'
    >>> bytes(s)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: string argument without an encoding
    >>> 
    >>> b = b'spam'
    >>> b.decode()
    'spam'
    >>> str(b, encoding='ascii')
    'spam'
    >>> str(b)
    "b'spam'"
    >>> len(str(b))
    7
    >>> len(str(b, encoding='ascii'))
    4
    
    >>> s = 'xyz'
    >>> s, len(s)
    ('xyz', 3)
    >>> [ord(c) for c in s]
    [120, 121, 122]
    >>> s.encode('ascii') # values 0...127 in 1 byte (7 bits) each
    b'xyz'
    >>> s.encode('latin-1') # values 0...255 in 1 byte (8 bits) each
    b'xyz'
    >>> s.encode('utf-8') # values 0..127 in 1 bute, 128...2047 in 2, others 3 or 4
    b'xyz'
    >>> s.encode('latin-1')[0]
    120
    >>> list(s.encode('latin-1'))
    [120, 121, 122]
    
    
    >>> chr(0xc4) # outside ascii's range
    'Ä'
    >>> chr(0xe8) 
    'è'
    >>> s = '\xc4\xe8' # single byte 8-bit hex escapes
    >>> s
    'Äè'
    >>> s = '\u00c4\u00e8' # 16-bit Unicode escapes
    >>> s
    'Äè'
    >>> len(s) # 2 characters long (not number of bytes!)
    2
    
    
    >>> s.encode('ascii')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    >>> s.encode('latin-1')
    b'\xc4\xe8'
    >>> s.encode('utf-8')
    b'\xc3\x84\xc3\xa8'
    >>> len(s.encode('latin-1'))
    2
    >>> len(s.encode('utf-8'))
    4
    
    
    >>> b = b'\xc4\xe8'
    >>> b
    b'\xc4\xe8'
    >>> len(b)
    2
    >>> b.decode('latin-1')
    'Äè'
    >>> b = b'\xc3\x84\xc3\xa8'
    >>> len(b)
    4
    >>> b.decode('utf-8')
    'Äè'
    >>> len(b.decode('utf-8'))
    2
    
    >>> s = 'A\u00c4B\U000000e8c'
    >>> s
    'AÄBèc'
    >>> len(s)
    5
    >>> s.encode('latin-1')
    b'A\xc4B\xe8c'
    >>> len(s.encode('latin-1'))
    5
    >>> s.encode('utf-8')
    b'A\xc3\x84B\xc3\xa8c'
    >>> len(s.encode('utf-8'))
    7
    
    >>> s = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
    >>> s
    'AÄBèC'
    >>> s = 'A\xC4B\xE8C'
    >>> s
    'AÄBèC'
    >>> s = 'A\u00C4B\U000000E8C'
    >>> s
    'AÄBèC'
    >>> b = b'A\xC4B\xE8C'
    >>> b
    b'A\xc4B\xe8C'
    >>> b = b'A\u00C4B\U000000E8C'
    >>> b
    b'A\\u00C4B\\U000000E8C'
    >>> b = b'A\xC4B\xE8C'
    >>> b
    b'A\xc4B\xe8C'
    >>> print(b)
    b'A\xc4B\xe8C'
    >>> b.decode('latin-1')
    'AÄBèC'

    >>> s = 'AÄBèC'
    >>> s
    'AÄBèC'
    >>> b = b'AÄBèC'
    File "<stdin>", line 1
    SyntaxError: bytes can only contain ASCII literal characters.
    >>> b = b'A\xC4B\xE9C'
    >>> b
    b'A\xc4B\xe9C'
    >>> b.decode('latin-1')
    'AÄBéC'
    >>> s.encode()
    b'A\xc3\x84B\xc3\xa8C'
    >>> s.encode('utf-8')
    b'A\xc3\x84B\xc3\xa8C'
    >>> b.decode()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc4 in position 1: invalid continuation byte
    >>> 
    
    """
    
    
def exampleBytes():
    """
    >>> set(dir('abc'))-set(dir(b'abc'))
    {'isprintable', 'isnumeric', 'casefold', 'isdecimal', 'isidentifier', 'format', 'format_map', 'encode'}
    >>> b = b'spam'
    >>> b.find(b'pa')
    1
    >>> b.replace(b'pa', b'XY')
    b'sXYm'
    >>> b.split(b'pa')
    [b's', b'm']
    >>> b
    b'spam'
    >>> b[0]
    115
    >>> b[0] = 'x'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'bytes' object does not support item assignment
    >>> b'%s' % 99
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'int'
    >>> b'{0}'.format(99)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'bytes' object has no attribute 'format'
    
    >>> b = b'abc'
    >>> b = bytes('abc', 'ascii')
    >>> b = bytes([97,98,99])
    """
    
    
def exampleBytearray():
    """
    >>> s = 'spam'
    >>> c = bytearray(s)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: string argument without an encoding
    >>> c = bytearray(s, 'latin1')
    >>> c
    bytearray(b'spam')
    >>> 
    >>> b = b'spam'
    >>> c = bytearray(b)
    >>> c
    bytearray(b'spam')
    >>> 
    >>> c[0]
    115
    >>> c[0] = 'x'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object cannot be interpreted as an integer
    >>> c[0] = b'x'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'bytes' object cannot be interpreted as an integer
    >>> c[0] = ord('x')
    >>> c[1] = b'Y'[0]
    >>> c.append(b'LMN')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'bytes' object cannot be interpreted as an integer
    >>> c.append(ord('L'))
    >>> c.extend(b'MNO')
    >>> c
    bytearray(b'xYamLMNO')
    >>> 
    >>> c + b'!#'
    bytearray(b'xYamLMNO!#')
    >>> len(c)
    8
    >>> c.replace('xY', 'sp')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: a bytes-like object is required, not 'str'
    >>> c.replace(b'xY', b'sp')
    bytearray(b'spamLMNO')
    >>> c * 2
    bytearray(b'xYamLMNOxYamLMNO')
    """
    
    
def exampleStruct():
    """
    >>> import struct
    >>> b = struct.pack('>i4sh', 7, b'spam', 8)
    >>> b
    b'\x00\x00\x00\x07spam\x00\x08'
    >>> vals = struct.unpack('>i4sh', b)
    >>> vals
    (7, b'spam', 8)
    >>> vals = struct.unpack('>i4sh', b.decode())
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: a bytes-like object is required, not 'str'
    >>> import struct
    >>> b = struct.pack('>i4sh', 7, b'spam', 8)
    >>> f = open('data.bin', 'wb')
    >>> f.write(b)
    10
    >>> f.close()
    >>> f = open('data.bin', 'rb')
    >>> data = f.read()
    >>> data
    b'\x00\x00\x00\x07spam\x00\x08'
    >>> values = struct.unpack('>i4sh', data)
    >>> values
    (7, b'spam', 8)
    >>> bin(values[0])
    '0b111'
    >>> values[0] & 0x01
    1
    >>> values[0] | 0b1010
    15
    >>> bin(values[0] | 0b1010)
    '0b1111'
    >>> bool(values[0] | 0b1010)
    True
    """