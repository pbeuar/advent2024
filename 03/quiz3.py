#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:53:27 2024

@author: pbeuar
"""

import re

with open('input') as f:
    input = f.read()


multis = re.findall(r'mul\((\d+,\d+)\)', input)

def mul(group:str):
    x,y = [int(x) for x in group.split(',')]
    # print(f'{x} x {y} = {x*y}')
    return x*y

answer1 = sum([mul(x) for x in multis])
# 191183308

#remove all input between all 'dont()' and 'do()'

line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def clean_input(lines:str):
    cleaned = ""
    lastdont = 0
    lastdo = 0
    
    while True:
        start = lines.find("don't()", lastdont)
        if start < 0:
            # add remaining text
            break
        end = lines.find("do()", start)
        if end < 0 :
            break
        # cleaned += lines[:lastdont] + lines[]
            
    
    
    
    
    
    
