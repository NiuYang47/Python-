# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:55:40 2020

@author: hasee
"""

keren = ['gk','qiezi','lbw','pdd','dasima']
mes0 = "请 " + keren[0] + " 来吃饭"
mes1 = "请 " + keren[1] + " 来吃饭"
mes2 = "请"  + keren[2] + " 来吃饭"
mes3 = "请 " + keren[3] + " 来吃饭"
mes4 = "请 " + keren[4] + " 来吃饭"
bulai = 'pdd'
keren.remove(bulai)
keren.insert(3, 'wdnmd')
print(mes0)
print(mes1)
print(mes2)
print(mes3)
print(mes4)
print(bulai + "来不了")
