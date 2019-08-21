#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


""" Broadcasting 

the smaller array is “broadcast” across the larger array so that they have compatible shapes.
Two dimensions are compatible when
    they are equal, or one of them is 1
    When either of the dimensions compared is one, the other is used.


    >>> a = np.array([1.0, 2.0, 3.0])
    >>> b = 2.0
    >>> a * b
    array([ 2.,  4.,  6.])


    >>> x = np.arange(4)
    >>> xx = x.reshape(4,1)
    >>> y = np.ones(5)
    >>> z = np.ones((3,4))
    >>> x.shape
    (4,)
    >>> y.shape
    (5,)
    >>> x + y
    ValueError: operands could not be broadcast together with shapes (4,) (5,)
    >>> x[:, np.newaxis] + y
    >>> xx.shape
    (4, 1)
    >>> y.shape
    (5,)
    >>> (xx + y).shape
    (4, 5)
    >>> x.shape
    (4,)
    >>> z.shape
    (3, 4)
    >>> (x + z).shape
    (3, 4)

"""
