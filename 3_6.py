# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:15:23 2020

@author: hasee
"""

keren = ['gk','qiezi','lbw']
keren.insert(0, 'cks')
keren.insert(1, 'mzd')
keren.append('gknmb')
zou_0 = keren.pop()
mes0 ="抱歉 " + zou_0 + " 不能参加吃饭" 
print(mes0)
zou_1 = keren.pop()
mes1 ="抱歉 " + zou_1 + " 不能参加吃饭" 
print(mes1)
zou_2 = keren.pop()
mes2 ="抱歉 " + zou_2 + " 不能参加吃饭" 
print(mes2)
zou_3 = keren.pop()
mes3 ="抱歉 " + zou_3 + " 不能参加吃饭"
print(mes3)
yaoqing_1 = keren[0]
print("你仍可以来 "+ yaoqing_1 )
yaoqing_2 = keren[1]
print("你仍可以来 "+ yaoqing_2 )
del keren[0]
print(keren)
print("桌子到不了只能来两个")