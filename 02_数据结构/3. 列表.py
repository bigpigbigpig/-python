# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 3. 列表.py
@time: 2019/07/29 21:34:26
"""

from array import array
from random import random

# list
list.sort([2, 3, 4])  # 不会创建新的列表
sorted([3, 4, 5])  # 会创建新的列表

import bisect
import sys

HAYSTACK = [1,4, 5,6, 7, 8, 12, 24, 55, 78]
NEEDLES = [0, 1, 2, 3, 5, 6, 75]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
print(ROW_FMT)

# 当列表是不是首选的时候，so 什么时候列表不是首选
# 数组背后存放的不是float对象，是翻译的字节码
# 如果对序列频繁的做先进先出的操作，双端队列的速度更快一些

floats = array('d', (random() for i in range(10*7)))
fp = open('dual', 'wb')
# 字节码代码的意思，写与读文件？

# 快速序列化数字类型的方法是使用 pickle.dump

# 内存视图其实是泛化和去数学化的numpy的数组，这个功能在处理大型数据集合的
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)

