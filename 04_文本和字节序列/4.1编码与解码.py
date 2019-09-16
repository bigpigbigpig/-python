# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 4.1编码与解码.py
@time: 2019/09/16 21:51:13
"""

# 示例编码与解码
s = 'cafγ'
print(len(s))
b = s.encode('utf-8')
print(b)
print(len(b))

