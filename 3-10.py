# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:42:38 2020

@author: hasee
"""

cccp = ['ak','rpg','rpk','t72','tu160']
mes = "I like " + cccp[2].title()
print(mes)
cccp[3] = 't80'
cccp.append('tu154')
print(cccp)
cccp.insert(0,'t34')
print(cccp)
cccp.remove('ak')
print(cccp)
cccp.sort()
print(cccp)
