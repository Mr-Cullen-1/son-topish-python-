# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:59:41 2024

@author: user
"""
import random


def son_top_pc(x=10):
    input(f"Endi siz 1 dan {x} gacha bo'lgan son o'ylang men topaman \n"
          "Boshlash uchun istalgan tugmani bosing!")
    minimum = 1
    maximum = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if minimum != maximum:
            taxmin = random.randint(minimum, maximum)
        else:
            taxmin = minimum
        javob = input(f"\nSiz {taxmin} sonini o'yladingiz. To'gri(t) \n"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-) > ")
        if javob == '-':
            maximum = taxmin - 1
        elif javob == '+':
            minimum = taxmin + 1
        elif javob =='t':
            break
    print(f"\nMen {taxminlar} ta urunishda topdim!")
    return taxminlar