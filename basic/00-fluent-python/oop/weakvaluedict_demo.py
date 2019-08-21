#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == "__main__":
    import weakref
    stock = weakref.WeakValueDictionary()  # 值是弱引用
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
               Cheese('Brie'), Cheese('Parmesan')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))  # 大多数不见了，这是WeakKeyDictionary的预期行为
    del cheese
    print(sorted(stock.keys()))
