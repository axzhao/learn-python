#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def example():
    """
    >>> import frenchdeck

    >>> beer_card = frenchdeck.Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')

    >>> deck = frenchdeck.FrenchDeck()
    >>> len(deck)
    52
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

