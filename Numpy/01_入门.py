# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 01_入门.py
@time: 2019/09/05 21:31:51
"""

# 创建一个列表

import numpy as np
g = list(range(10000))

g_array = np.array(g)

a = np.array([1,2,3,4,5])
print(a.shape)
print(a.ndim)

