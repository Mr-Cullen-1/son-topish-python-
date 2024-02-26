# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:16:12 2024

@author: Jacob
Topic: 'Son topish' dasturi
"""

import son_top1 as part_1
import son_top2 as part_2

def play(x=10):
    flag = True
    while flag:
        taxminlar_user = part_1.son_top()
        taxminlar_pc = part_2.son_top_pc()
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        flag = int(input("Yana o'ynaymizmi? Ha(1) / Yo'q (0): "))
        
play()