#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":
    city = '哈！'
    print(city.encode('utf8'))  # b'\xe5\x93\x88\xef\xbc\x81'
    # \xff\xfe BOM，字节序标记 byte-order mark，指明编码时使用Intel CPU的小字节序
    print(city.encode('utf16'))  # b'\xff\xfe\xc8T\x01\xff'
    # print(city.encode('cp437')) # UnicodeEncodeError
    print(city.encode('cp437', errors='ignore'))
    print(city.encode('cp437', errors='replace'))
    print(city.encode('cp437', errors='xmlcharrefreplace'))

    octets = b'\xe5\x93\x88\xef\xbc\x81'
    print(octets.decode('utf8'))
    print(octets.decode('utf16'))
    print(octets.decode('cp437', errors='replace'))

    print("\n处理文本文件")
    fp = open('cafe.txt', 'w', encoding='utf8')
    print(fp)
    fp.write(city)
    fp.close()
    import os
    print(os.stat('cafe.txt').st_size)
    fp2 = open('cafe.txt')
    print(fp2)
    print(fp2.encoding)
    print(fp2.read())
    fp3 = open('cafe.txt', encoding='utf8')
    print(fp3)
    print(fp3.read())
    fp4 = open('cafe.txt', 'rb')
    print(fp4)
    print(fp4.read())

    print("\n编码默认值")
    import sys
    import locale
    expressions = """
        locale.getpreferredencoding()
        type(f)
        f.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
    f = open('cafe.txt', 'w')
    for expression in expressions.split():
        value = eval(expression)
        print(expression.rjust(30), '->', repr(value))

    print("\nUnicode字符串")
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(len(s1), len(s2))
    print(s1 == s2)
    print(id(s1), type(s1))
    print(id(s2), type(s2))

    print("\nUnicode数据库")
    import unicodedata
    import re
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u126b\u216b\u2466\u2480\u3285'
    for char in sample:
        print('U+%04x' % ord(char),
              char.center(6),
              're_dig' if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(unicodedata.numeric(char),
                     '5.2f') if char.isnumeric() else 0.00,
              unicodedata.name(char),
              sep='\t')

    print("\n支持字符串和字节序列的双模式API")
    import re
    re_numbers_str = re.compile(r'\d+')
    re_words_str = re.compile(r'\w+')
    re_numbers_bytes = re.compile(rb'\d+')
    re_words_bytes = re.compile(rb'\w+')
    text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
                " as 2⁴.")
    text_bytes = text_str.encode("utf8")
    print("Text", repr(text_str), sep='\n   ')
    print('Numbers')
    print(' str  :', re_numbers_str.findall(text_str))
    print(' bytes:', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print(' str  :', re_words_str.findall(text_str))
    print(' bytes:', re_words_bytes.findall(text_bytes))
    import os
    print(os.listdir('.'))
    print(os.listdir(b'.'))
    pi_name_bytes = os.listdir(b'.')[0]
    pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
    print(pi_name_str)
    print(pi_name_str.encode('ascii', 'surrogateescape'))
