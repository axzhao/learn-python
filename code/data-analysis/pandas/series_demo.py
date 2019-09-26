#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import numpy as np
import pandas as pd

""" Series  

s = pd.Series(data, index=index)

input data type: array-like, iterable, dict, or scalar value
a python dict
    index == None || != || == len(data)，截断/ Nan
    pd.Series({'b': 1, 'a': 0, 'c': 2})
an ndarray
    index == None || len(data)，一一匹配
    pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
a scalar value
    index != None || != || == len(data)，重复匹配
    pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])

notes:
1. pandas supports non-unique index values. if an operation that does not support duplicate index values is aattemped, an exception will be raised at that time.
2. when the data is a dict, and an index is not passed, the Series index will be orded by the dict's insertion order.

"""

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s1 = pd.Series(np.random.randn(5), name='something')
s1.name
s2 = s1.rename("different")
s2.name

""" Series is ndarray-like """

s[0]
s[:3]
s[s > s.median()]
s[[4, 3, 1]]  # indexing
np.exp(s)
s.dtype  # a NumPy dtype or ExtensionDtype

# Series.array
# the actual array backing a Series
# useful when to do some operation without the index
# always be an ExtensionArray
s.array

# even if the Series is backed by a ExtensionArray, it will return a Numpy ndarray.
s.to_numpy()

""" Series is dict-like """

s['a']
s['e'] = 12
'e' in s
'f' in s  # if a label is not contained, KeyError
s.get('f')
s.get('f', np.nan)


dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

""" Vectorized operations and label alignment with Series """

s + s
s * 2
np.exp(s)

# A key difference between Series and ndarray is that operations between Series automatically align the data based on label.
s[1:] + s[:-1]


ser = pd.Series([1, 2, 3])
idx = pd.Index([4, 5, 6])
np.maximum(ser, idx)
