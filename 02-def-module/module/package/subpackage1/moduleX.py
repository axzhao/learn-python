#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

print('in mod.py')
z = 3

# 同包
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY

# 上一级
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo

# 上上级
from ...package import bar