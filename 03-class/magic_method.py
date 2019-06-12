#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
magic method
    __xxx__ 方法，语言层面交互
    迭代，集合类，属性访问，运算符重载，对象的创建和销毁，字符串表示形式和格式化，管理上下文with块

"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # 会忽略代码里[],{},()中的换行
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    # 为什么len不是普通的方法，因为len(x)快，CPython直接从C结构体里读取对象长度
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    # __len__
    deck = FrenchDeck()
    print(len(deck))
    
    # __getitem__
    print(deck[0])
    print(choice(deck))

    # __iter__
    for card in deck:
        print(card)
    for card in reversed(deck):
        print(card)
    print(Card('Q', 'hearts') in deck)
    # order
    for card in sorted(deck, key=spades_high):
        print(card)