# !/usr/bin/env python# -- coding:utf-8 --# 小猫爱吃鱼，小猫要喝水class Cat:    '''cat link eat fish.    cat need drink water.    '''    def __init__(self):        print("This is a init function.")    def eat(self):        print("%s like eat fish." % self.name)    def drink(self):        print("cat need drink water.")    def play(what):        print("%s play what" % what)tom = Cat()tom.name = "Tom"tom.eat()# __init__() 初始化方法定义类中有哪些对象# 当使用类名（）会自动调用初始化方法# 创建对象时，会自动创建初始化方法# 创建对象时，会自动创建初始化方法# 创建对象时，会自动创建初始化方法