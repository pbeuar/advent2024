from itertools import product

with open('input') as f:
    data = f.read()

lines = [[x.strip() for x in line.partition(":") if x != ':'] for line in data.splitlines()]


def operation(x, y, oper):
    if oper == 0:
        return x + y
    elif oper ==1:
        return x * y
    else:
        return int(str(x)+str(y))


answer = 0
# 7885693428401

for line in lines:
    target = int(line[0])
    nums = [int(x) for x in line[1].split()]    
    n = len(nums)-1
    opers = [list(x) for x in product([0, 1], repeat=n)]
    base = nums.pop(0)
    for op in opers:
        total = base
        for o, num in zip(op,nums):
            total = operation(total, num, o)
        if total == target:
            answer += total
            break

answer2 = 0
# 348360680516005

for line in lines:
    target = int(line[0])
    nums = [int(x) for x in line[1].split()]    
    n = len(nums)-1
    opers = [list(x) for x in product([0, 1, 2], repeat=n)]
    base = nums.pop(0)
    for op in opers:
        total = base
        for o, num in zip(op,nums):
            total = operation(total, num, o)
        if total == target:
            answer2 += total
            break

                
