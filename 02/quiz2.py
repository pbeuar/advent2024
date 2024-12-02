#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:25:14 2024

@author: pbeuar

day2
all increasing or all decreasing.
1~3

1- How many reports are safe?
"""


reports = []

with open('input') as f:
    for line in f:
        reports.append([int(x) for x in line.strip().split()])


diffs = []

for report in reports:
    diffs.append([report[x]-report[x+1] for x in range(len(report)-1)])



def gap(report):
    if 0 in report:
        return False
    report_plus = [abs(x) for x in report]
    return min(report_plus) >= 1 and max(report_plus) <= 3

def all_increasing_or_decreasing(report):
    first = report[0] > 0
    for diff in report[1:]:
        if not (diff > 0) == first:
            return False
    return True


answer1 = len([x for x in diffs if gap(x) and all_increasing_or_decreasing(x)])











    