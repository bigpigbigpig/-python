# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 3.3 用setdefault处理找不到的键.py
@time: 2019/09/04 22:05:54
"""

# 从索引中获取单词出现的频率信息，并把它们写进对应的列表中
# 举例
import sys
import re

WORE_RE = re.compile(r'\w+')
print(WORE_RE)

index = {}

with open(r'test.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORE_RE.finditer(line):

            print({line_no: line})
