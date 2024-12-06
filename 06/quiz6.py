#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:30:28 2024

@author: pankusher
"""

with open('input') as f:
    data = [[x for x in y] for y in f.read().split()]



width  = len(data[0])
height = len(data)

arrows = ['^', '>', 'v', '<']

dirs = [
        (0,-1),
        (1, 0),
        (0, 1),
        (-1,0)
        ]



def find_guard(data):
    for y, h in enumerate(data):
        for arr in arrows:
            if arr in h:
                return [h.index(arr), y, dirs[arrows.index(arr)]]


x, y, g_dir = find_guard(data)

def add_dir(g, d):
    return (g[0]+d[0], g[1]+d[1]) 


# change dir - (dir+1)%4 or in degrees dir +90 and atan2
positions = 1

while True:
    xx, yy = add_dir((x,y), g_dir)
    if xx < width and xx >= 0 and yy < height and yy >= 0:
        if data[yy][xx] == '#':
            g_dir = dirs[(dirs.index(g_dir)+1)%4]
        else:
            x,y = xx,yy
            if data[y][x] == '.':
                data[y][x] = 'X'
                positions+=1
    else:
        print(positions)
        print(x,y,g_dir)
        break
    
answer1 = positions

