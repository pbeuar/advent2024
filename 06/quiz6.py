import copy


with open('input') as f:
    data = [[x for x in y] for y in f.read().split()]

data2 = copy.deepcopy(data)


width  = len(data[0])
height = len(data)

arrows = ['^', '>', 'v', '<']

dirs = [
       (0,-1),
       (1, 0),
       (0, 1),
       (-1,0)
       ]

positions = []

def find_guard(data):
    for y, h in enumerate(data):
        for arr in arrows:
            if arr in h:
                return [y, h.index(arr), dirs[arrows.index(arr)]]
 

y, x, g_dir = find_guard(data)
positions.append([y, x])

def add_dir(g, d):
    return (g[0]+d[0], g[1]+d[1]) 


while True:
    xx, yy = add_dir((x,y), g_dir)
    if xx < width and xx >= 0 and yy < height and yy >= 0:
        if data[yy][xx] in '#O':
            g_dir = dirs[(dirs.index(g_dir)+1)%4]
        elif data[yy][xx] == arrows[dirs.index(g_dir)]:
            print("loop")
            break
        else:
            x,y = xx,yy
            if data[y][x] == '.':
                data[y][x] = arrows[dirs.index(g_dir)]
                positions.append([y,x])
    else:
        break
    
answer1 = len(positions)
# 4374

blocks = []


for pos in positions[1:]:
    data_copy = copy.deepcopy(data2)
    y, x, g_dir = find_guard(data2)
    data_copy[pos[0]][pos[1]] = 'O'
    while True:
        xx, yy = add_dir((x,y), g_dir)
        if xx < width and xx >= 0 and yy < height and yy >= 0:
            if data_copy[yy][xx] in '#O':
                g_dir = dirs[(dirs.index(g_dir)+1)%4]
            elif data_copy[yy][xx] == arrows[dirs.index(g_dir)]:
                #if direction is the same as the arrow ->> it's a loop
                blocks.append(pos)
                break
            else:
                x,y = xx,yy
                if data_copy[y][x] == '.':
                    data_copy[y][x] = arrows[dirs.index(g_dir)]
        else:
            break


answer2 = len(blocks)
#1705

