#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def exampleFloat():
    """
    >>> num = 1 / 3.0
    >>> print(num)
    0.3333333333333333
    >>> '%e' % num
    '3.333333e-01'
    >>> '%4.2f' % num
    '0.33'
    >>> '{0:4.2f}'.format(num)
    '0.33'
    >>> n1 = n2 = n3 = 2
    >>> print(n1,n2,n3)
    2 2 2
    """

def exampleNumeric():
    """
    >>> a = 6
    >>> print(a, hex(a), oct(a), bin(a))
    (6, '0x6', '06', '0b110')
    >>> print('{0:o},{1:x},{2:b}'.format(64,64,64))
    100,40,1000000
    """

def exampleChainedComparisions():
    """
    >>> x, y, z = 1, 2, 3
    >>> print(x<y<z, x<y and y<x) 
    True False
    >>> print(1==2<3, 1==2 and 2<3)
    False False 
    """

def exampleDivide():
    """
    >>> print(5/2,5/2.0,5/-2,5/-2.0)
    (2, 2.5, -3, -2.5)
    >>> print(5//2,5//2.0,5//-2,5//-2.0)
    (2, 2.0, -3, -3.0)
    >>> import math
    >>> math.floor(2.5)
    2
    >>> math.floor(-2.5)
    -3
    >>> math.trunc(2.5)
    2
    >>> math.trunc(-2.5)
    -2
    """

def exampleDecimal():
    """
    >>> import decimal
    >>> decimal.Decimal('1.00')/decimal.Decimal('3.00')
    Decimal('0.3333333333333333333333333333')
    >>> with decimal.localcontext() as ctx:
    ...     ctx.prec=2
    ...     decimal.Decimal('1.00')/decimal.Decimal('3.00')
    Decimal('0.33')
    >>> decimal.Decimal('1.00')/decimal.Decimal('3.00')
    Decimal('0.3333333333333333333333333333')
    >>> 0.1+0.1+0.1-0.3
    5.551115123125783e-17
    >>> from decimal import Decimal
    >>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
    Decimal('0.0')
    """

def exampleFraction():
    """
    >>> from fractions import Fraction
    >>> print(Fraction(1,3))
    1/3
    """

def exampleConv():
    """
    >>> (2.5).as_integer_ratio()
    (5, 2)
    >>> f = 2.5
    >>> z = Fraction(*f.as_integer_ratio())
    >>> z
    Fraction(5, 2)
    >>> Fraction.from_float(1.75)
    Fraction(7, 4)
    >>> x = Fraction(1,3)
    >>> a = x + Fraction(*(4.0/3).as_integer_ratio())
    >>> a
    Fraction(22517998136852479, 13510798882111488)
    >>> a.limit_denominator(10)
    Fraction(5, 3)
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

