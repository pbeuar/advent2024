
with open('input') as f:
    data_map = [[int(x) for x in y] for y in f.read().splitlines()]


# look for 0. mark as root. (look in all directions for 0 +1 add to zero)
# when reaches 9 add coor to the 0 entry in trails dict
# ? naybe need to keep end trails for less computations 

