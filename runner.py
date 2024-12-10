
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

data_map = [[int(x) for x in y] for y in data_map.splitlines()]


# look for 0. mark as root. (look in all directions for 0 +1 add to zero)
# when reaches 9 add coor to the 0 entry in trails dict
# ? naybe need to keep end trails for less computations 

