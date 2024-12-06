import copy


data_txt = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    
# data = [x for x in data_txt.split()]

data = [[x for x in y] for y in data_txt.split()]
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


# change dir - (dir+1)%4 or in degrees dir +90 and atan2


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
        print(x,y,g_dir)
        break
    
answer1 = len(positions)

blocks = []

maps = []



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
                print("loop")
                blocks.append(pos)
                maps.append(data_copy)
                break
            else:
                x,y = xx,yy
                if data_copy[y][x] == '.':
                    data_copy[y][x] = arrows[dirs.index(g_dir)]
        else:
            # print(x,y,g_dir)
            print('out')
            break















