#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exSort():
    """
    >>> fruits = ['grape', 'raspberry', 'apple', 'banana']
    >>> sorted(fruits)
    ['apple', 'banana', 'grape', 'raspberry']
    >>> fruits
    ['grape', 'raspberry', 'apple', 'banana']
    >>> sorted(fruits, reverse=True)
    ['raspberry', 'grape', 'banana', 'apple']
    >>> fruits
    ['grape', 'raspberry', 'apple', 'banana']
    >>> sorted(fruits, key=len)
    ['grape', 'apple', 'banana', 'raspberry']
    >>> fruits
    ['grape', 'raspberry', 'apple', 'banana']
    >>> sorted(fruits, key=len, reverse=True)
    ['raspberry', 'banana', 'grape', 'apple']
    >>> fruits
    ['grape', 'raspberry', 'apple', 'banana']
    >>> fruits.sort()
    >>> fruits
    ['apple', 'banana', 'grape', 'raspberry']
    """

def exBisect():
    """
    
    """



if __name__ == "__main__":
    import doctest
    doctest.testmod()

