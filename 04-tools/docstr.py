#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"
    def method(self, args):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass

def exampleDocstr():
    """
    >>> import docstr
    >>> docstr.__doc__
    'I am: docstr.__doc__'
    >>> docstr.func.__doc__
    'I am: docstr.func.__doc__'
    >>> docstr.spam.__doc__
    'I am: spam.__doc__ or docstr.spam.__doc__'
    >>> docstr.spam.method.__doc__
    'I am: spam.method.__doc__ or self.method.__doc__'

    # help(docstr)
    """