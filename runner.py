
data_map = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
"""
[[8, 9, 0, 1, 0, 1, 2, 3],
 [7, 8, 1, 2, 1, 8, 7, 4],
 [8, 7, 4, 3, 0, 9, 6, 5],
 [9, 6, 5, 4, 9, 8, 7, 4],
 [4, 5, 6, 7, 8, 9, 0, 3],
 [3, 2, 0, 1, 9, 0, 1, 2],
 [0, 1, 3, 2, 9, 8, 0, 1],
 [1, 0, 4, 5, 6, 7, 3, 2]]
"""

nines = 0
zeros = 0



data = [[int(x) for x in y] for y in data_map.splitlines()]


height = len(data_map)
width = len(data_map[0])


dirs = [
       (0,-1),
       (1, 0),
       (0, 1),
       (-1,0)
       ]


trails = {}

trail_id = 0

# look for 0. mark as root. (look in all directions for 0 +1 add to zero)
# when reaches 9 add coor to the 0 entry in trails dict
# ? naybe need to keep end trails for less computations 

def add_dir(g, d):
    return (g[0]+d[0], g[1]+d[1]) 

def out_of_bounds(opt):
    return opt[0] < 0 or opt[0] >= height or opt[1] < 0 or opt[1] >= width


def can_climb(y,x,v):
    res = []
    for d in dirs:
        opt = add_dir((y,x), d)
        if not out_of_bounds(opt) and data[opt[0]][opt[1]] == v+1:
            res.append(opt)
    return res


for y, row in enumerate(data):
    for x, peak in enumerate(row):
        if peak == 0:
            trails[trail_id] = []
            
            
            




















