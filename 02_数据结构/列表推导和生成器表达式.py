# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 列表推导和生成器表达式.py
@time: 2019/07/22
"""
import collections

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

# 元组拆包
# 元组拆包可以应用到任何可迭代对象上，
divmod(10, 2)  # 学习一个新的函数
# 元组拆包的用法是让一个函数可以用元组的形式返回多个值，

# _ 经常是常用函数 gettext.gettext函数的常用名
# 可以使用 *var 来代替 _
a, b, *var = range(10)
print(a, b, var)

# 另外一种形式的元组拆包
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),  # ➊
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # ➋
    if longitude <= 0: # ➌
        print(fmt.format(name, latitude, longitude))

# 具名元组 collections.namedtuple 是一个工厂函数，构建一个带字段名的元组和一个有名字的鳄梨
# 决定使用具名元组来存放相位饱和度
# 存放在对应字段里的数据要以一串参数的形式传入到构造函数中，可以当一个类来使用

PhaseC = collections.namedtuple('PhaseC', 'date dayplan num data')  # 时段号，第几个5分钟，相位饱和度（）
ls = [PhaseC('date', 'dayplan', 'num', 'data'), PhaseC('...'), ]  # 放一天的数据

'''
if dates is None => conclusion 1
for date in dates: # if just one, so split date not dates
    ready phase_tuple data
    if tuple is None => conclusion 4  # before add raise on get oracle data, base on other devloper
    day_info is True
    for i in day_info:
        if is i.min_green and i.fix_phase
            delete phase in phase_tuple
        add(phase_tuple_of_day_plan) / k >=< O  => conclusion 2 or conlcusion 3
'''

# 1. get_info => _fiels() show all shuxing _asdict() show all data

