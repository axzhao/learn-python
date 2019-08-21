#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import re
import collections
WORD_RE = re.compile(r'\w+')


def noKeyFunc1And2():
    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                # 这其实是一种很不好的实现，这样写只是为了证明论点
                # index.setdefault(word, []).append(location)
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
    # 以字母顺序打印出结果
    for word in sorted(index, key=str.upper):
        print(word, index[word])


def noKeyFunc3():
    index = collections.defaultdict(list)
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                index[word].append(location)
    # 以字母顺序打印出结果
    for word in sorted(index, key=str.upper):
        print(word, index[word])


class StrKeyDict0(dict):

    def __missing__(self, key):
        """为什么isinstance(key, str)测试在dunder-missing中是必需的

        如果没有这个测试，只要 str(k) 返回的是一个存在的键，
        那么__missing__ 方法是没问题的，
        不管是字符串键还是非字符串键，它都能正常运行。

        但是如果 str(k) 不是一个存在的键，代码就会陷入无限递归。
        这是因为 __missing__ 的最后一行中的 self[str(key)] 会调用 __getitem__，
        而这个 str(key) 又不存在，于是 __missing__又会被调用。
        """
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # 改写 get 方法，好让它的表现跟 __getitem__ 一致
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        """为了保持一致性，__contains__ 方法在这里也是必需的。

        这是因为 k in d 这个操作会调用它，但是我们从 dict 继承到的 __contains__
        方法不会在找不到键的时候调用 __missing__ 方法。__contains__
        里还有个细节，就是我们这里没有用更具 Python 风格的方式——k in
        my_dict——来检查键是否存在，因为那也会导致 __contains__ 被递
        归调用。为了避免这一情况，这里采取了更显式的方法，直接在这个
        self.keys() 里查询。

        出于对准确度的考虑，我们也需要这个按照键的原本的值来查找的操作
        （也就是 key in self.keys()），因为在创建 StrKeyDict0 和为它
        添加新值的时候，我们并没有强制要求传入的键必须是字符串。因为这
        个操作没有规定死键的类型，所以让查找操作变得更加友好。
        """
        return key in self.keys() or str(key) in self.keys()


if __name__ == "__main__":
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(a == b == c == d == e)

    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
    country_code = {country: code for code, country in DIAL_CODES}
    {code: country.upper() for country, code in country_code.items() if code < 66}
