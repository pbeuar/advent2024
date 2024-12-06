

list_a = []
list_b = []

with open('input') as f:
    for line in f:
        a, b = line.strip().split()
        list_a.append(int(a))
        list_b.append(int(b))

list_a.sort()
list_b.sort()



answer1 = sum([abs(x-y) for x,y in zip(list_a, list_b)])

# # 1319616

answer2 = sum([x * list_b.count(x) for x in list_a])

# 27267728