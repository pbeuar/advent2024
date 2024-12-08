

with open('input') as f:
    data_txt = f.read()

data = [[x for x in y] for y in data_txt.split()]

height = len(data)
width = len(data[0])

antenas = {}
nodes = []

for yi, y in enumerate(data):
    for xi, x in enumerate(y):
        if x.isalnum():
            if x not in antenas:
                antenas[x] = []
            antenas[x].append((yi,xi))


def calc_vec(a, b, plus):
    if plus:
        return (a[0] + b[0], a[1] + b[1])
    return (a[0] - b[0], a[1] - b[1])

def out_of_bounds(node):
    return node[0] < 0 or node[0] >= height or node[1] < 0 or node[1] >= width

def calc_antinodes(a, b):
    dist = calc_vec(a, b, False)
    an1 = calc_vec(a, dist, True)
    an2 = calc_vec(b, dist, False)
    for node in [an1,an2]:
        if not out_of_bounds(node):
            nodes.append(node)
    
    

for freq in antenas:
    amount = len(antenas[freq])
    for idx in range(amount-1):
        for sidx in range(idx+1, amount):
            calc_antinodes(antenas[freq][idx], antenas[freq][sidx])


answer1 = len(set(nodes))
# 289


nodes2 = []

def multiply_dist(node,factor):
    return (node[0] * factor, node[1] * factor)

def calc_antinodes2(a, b):
    dist = calc_vec(a, b, False)
    factor = 1
    while True:
        dist1 = multiply_dist(dist, factor)
        temp_node = calc_vec(a, dist1, True)
        if not out_of_bounds(temp_node):
            nodes2.append(temp_node)
            factor += 1
        else:
            break
    factor = 1
    while True:
        dist1 = multiply_dist(dist, factor)
        temp_node = calc_vec(a, dist1, False)
        if not out_of_bounds(temp_node):
            nodes2.append(temp_node)
            factor += 1
        else:
            break
    nodes2.append(a)
    nodes2.append(b)




for freq in antenas:
    amount = len(antenas[freq])
    for idx in range(amount-1):
        for sidx in range(idx+1, amount):
            calc_antinodes2(antenas[freq][idx], antenas[freq][sidx]) 
            
            
answer2 = len(set(nodes2))


























