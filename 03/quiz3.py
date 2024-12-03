#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:53:27 2024

@author: pbeuar
"""

import re

with open('input') as f:
    text = f.read()

# add up all of the results of the multiplications: mul(a,b)

multis = re.findall(r'mul\((\d+,\d+)\)', text)

def mul(group:str):
    x,y = [int(x) for x in group.split(',')]
    # print(f'{x} x {y} = {x*y}')
    return x*y

answer1 = sum([mul(x) for x in multis])
# 191183308


# remove all input between all 'dont()' and 'do()'

def clean_input(text:str):
    cleaned = ""
    lastdont = 0
    lastdo = 0
    
    while True:
        end = text.find("don't()", lastdo)
        if end < 0:
            cleaned += text[lastdo:]
            break
        cleaned += text[lastdo:end]
        lastdont = end + 7
        lastdo = text.find("do()", lastdont)

        if lastdo < 0 :
            break
    
    return cleaned

multis2 = re.findall(r'mul\((\d+,\d+)\)', clean_input(text))

answer2 = sum([mul(x) for x in multis2])
# 92082041

