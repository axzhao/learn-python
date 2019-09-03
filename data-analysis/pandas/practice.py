#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# %%
import pandas as pd
import numpy as np

d = {"A": ["a", np.nan, np.nan, "b", np.nan],
     "B": ["b1", "b2", np.nan, "c1", "c2"],
     "C": ["c1", "c2", "c3", "C4", "C5"],
     "D": [np.nan, np.nan, np.nan, "d1", "d2"]}

df = pd.DataFrame(d)
df[["A", "B"]] = df[["A", "B"]].ffill()
c = np.where(pd.isnull(df["D"]), df["D"], df["C"])
d = np.where(pd.isnull(df["D"]), df["C"], df["D"])
df["C"] = c
df["D"] = d
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
df["ID"] = df.index+1
print(df)

# %%
import pandas as pd

d = {"A": [" a ", " ", " c "],
     "B": ["", "", ""]}
df = pd.DataFrame(d)
df = df.apply(lambda x: x.str.strip())
df["source"] = "haha"
df["B"] = df["A"].apply(lambda x: x if x == "a" else "")
print(df)

#%%
import pandas as pd
from pyspark import SparkContext, SparkConf, HiveContext
from pyspark.sql.functions import *

sc.stop()
sc = SparkContext()
sqlContext = HiveContext(sc)

df1 = sqlContext.createDataFrame(
    [(1, "a", "aa", "aaa"), (2, "b", "bb", "bbb"), (3, "c", "cc", "ccc"), (4, "d", "dd", "ddd")],
    ("id", "c1", "c2", "c3"))

df2 = sqlContext.createDataFrame(
    [(1, "1", "11", "111", "p1"), (2, "2", "22", "", "p2"), (3, "3", "33", "", "p3")], 
    ("id", "p1", "p2", "p3", "p4"))

df3 = sqlContext.createDataFrame(
    [("a", "aa", "aaa", "p1", 0, 0), ("b", "bb", "bbb", "p1", 0, 0), ("c", "cc", "ccc", "p2", 0, 0), ("z", "zz", "", "p9", 0, 0)], 
    ("c1", "c2", "c3", "p4", "d1_id", "d2_id"))

df = df3.\
     join(df1, (df3.c1 == df1.c1) & (df3.c2 == df1.c2) & (df3.c3 == df1.c3), "inner").\
     join(df2, (df3.p4 == df2.p4), "inner").\
     select(col("*").aliax("id"), df3.c1, df3.c2, df3.c3, df3.p4, df1.id.alias("d1_id"), df2.id.alias("d2_id")).\
     filter((df1.id > 0) & (df2.id > 0))
df.show()
sc.stop()

#%%

from pyspark import SparkContext, SparkConf, HiveContext
from pyspark.sql.functions import *

sc.stop()
sc = SparkContext()
sqlContext = HiveContext(sc)

df1 = sqlContext.createDataFrame(
    [(1, "a", "aa", "aaa"), (2, "b", "bb", "bbb"), (3, "c", "cc", "ccc"), (4, "d", "dd", "ddd")],
    ("id", "c1", "c2", "c3"))

df2 = sqlContext.createDataFrame(
    [(1, "1", "11", "111", "p1"), (2, "2", "22", "", "p2"), (3, "3", "33", "", "p3")], 
    ("id", "p1", "p2", "p3", "p4"))

df3 = sqlContext.createDataFrame(
    [(1, "a", "aa", "aaa", "p1", 0, 0), (2, "b", "bb", "bbb", "p1", 0, 0), (3, "c", "cc", "ccc", "p2", 0, 0), (4, "z", "zz", "", "p9", 0, 0)], 
    ("id", "c1", "c2", "c3", "p4", "d1_id", "d2_id"))


df = df2.join(df3, (df2.p4 == df3.p4), "left")
df.show()
sc.stop()

#%%
