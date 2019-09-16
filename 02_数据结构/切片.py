# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 切片.py
@time: 2019/07/23 22:46:15
"""

# 对对象进行切片操作
s = 'bicycle'
print(s[::3])
print(s[::-1])

# 怎么自动对应到相应的代码上去的，这是一个值得研究的问题

# 多为切片和省略
# ... 是 类 ellipsis 的实例 Ellipsis对象
# 给切片赋值
l = list(range(10))
l[2:6] = [10]
print(l)
# 对序列使用 + *
print('abc' * 5)

# 如果进行数据操作的时候，对引用进行*操作
board = ['_'*3] * 3  # 对引用的赋值

# 序列的增量赋值
# __iadd__ += *= 