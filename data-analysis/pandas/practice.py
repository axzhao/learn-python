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
df["ID"] = df.index+1
print(df)

# %%
