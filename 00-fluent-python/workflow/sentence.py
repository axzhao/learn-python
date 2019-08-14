#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence1:
    """把句子划分为单词序列"""

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):  # 为了完善序列协议，实现了len方法，不过为了让对象可以迭代，没必要实现这个方法
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


def exampleS1():
    """
    >>> from sentence import *
    >>> s = Sentence1('"The time has come," the Walrus said,')
    >>> s
    Sentence('"The time ha... Walrus said,')
    >>> for word in s:
    ...     print(word)
    ... 
    The
    time
    has
    come
    the
    Walrus
    said
    >>> list(s)
    ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
    """


class Sentence2:
    """使用迭代器模式实现"""

    def __init__(self, text):
        self.text = text
        # self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # way 1:
        # return SentenceIterator(self.words)
        # way 2:
        # return iter(self.words)
        # way 3:
        # for word in self.words:
            # yield word
        # return  # 可要可不要
        # way 4:
        # re.finditer 是 re.findall 的惰性版本 lazy evaluation, eager evaluation
        # for match in RE_WORD.finditer(self.text):
        #   yield match.group()
        # way 5:
        return (match.group() for match in RE_WORD.finditer(self.text))


class SentenceIterator:
    """
    为了支持多种遍历，必须能从同一个可迭代的实例中获取多个独立的迭代器，而且各个迭代器要能维护自身的内部状态
    为了调用iter()都新建一个独立的迭代器
    更符合python习惯的方式是，用生成器函数代替SentenceIterator类
    """

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):  # 可以不用实现iter方法，不过这么做是对的，因为迭代器应该实现next和iter两个方法，而且这么做能让迭代器通过issubclass(SentenceIterator, abc.Iterator)测试。
        # 如果让SentenceIterator类继承abc.Iterator类，那么会继承abc.Iterator.__iter__这个具体方法。
        return self
