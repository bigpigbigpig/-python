# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 列表推导和生成器表达式.py
@time: 2019/07/22
"""

# 列表推导很强大
# 掌握列表推导还可以为我们打开 生成器表达式 的大门
# 生成器表达式 具有 生成个各种类型的元素 并用它们填充序列

# 列表推导和可读性
# 列表推导不会有变量泄露的问题
dict = {'b': 1, 'e': 3, 'f': 4, 'g': 5, 'h': 6}
dict_num = [dict[i] for i in 'bgefgh']
print(dict_num)

# 列表推导同 filter 和 map
# 效率：https://github.com/fluentpython/examplecode/blob/master/02-array-seq/listcomp_speed.py
# 双引号可以定义多行字符串
string = """
    hello, hello
    nice to meet you!
"""

# 列表推导2
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

# 列表推导的作用只是生成列表
# 生成其他类的行的序列，使用生成器表达式
# 生成器表达式的语法和列表推导差不多，只不过是将方括号换成圆括号
symbols = 'hjgshdj'
ge_ex = (ord(i) for i in symbols)
print(ge_ex)
# 是逐一产生元素的，避免额外的内存占用

