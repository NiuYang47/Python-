# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:00:00 2020

@author: hasee
"""

tanks = ['t64','m1a2','ztz99','tpye59'] 
his_tanks = tanks[:]
print(his_tanks)
his_tanks.append('t72')
print("My tanks: \n")
for tank in tanks:
    print(tank)
print("\n")    
print("His tank: ")    
for his_tank in his_tanks:
    print(his_tank)    
