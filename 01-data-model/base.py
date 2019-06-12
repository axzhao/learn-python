#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def numbers():
    print(8/5) # division always returns a floating point number

def strings():
    print('doesn\'t')
    print("doesn't")
    print("""\
        Usage: thingy [OPTIONS]
            -h                        Display this usage message
            -H hostname               Hostname to connect to
        """)
    print('''\
        Usage: thingy [OPTIONS]
            -h                        Display this usage message
            -H hostname               Hostname to connect to
        ''')
    print('Py' 'thon')  # can't concatenate a variable and a string literal
    print('Py' 
        'thon')

    word = 'Python'
    print(word[0])
    print(word[-1])    


if __name__ == "__main__":
    strings()