
data = '5 62914 65 972 0 805922 6521 1639064'  #'125 17'

stones = [int(x) for x in data.strip().split()]


def apply_rules(num):
    if num == 0:
        return [1]
    strnum = str(num)
    if len(strnum)%2 == 0:
        half = int(len(strnum)/2)
        return [int(strnum[:half]), int(strnum[half:])]
    return [num*2024]


for _ in range(25):
    new_stones = []
    for stone in stones:
        s = apply_rules(stone)
        new_stones += s
    
    stones = new_stones
    
answer1 = len(stones)
#199753

