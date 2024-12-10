
disk_map = open('input').read().strip()

blocks = []

ID = 0

for i, cell in enumerate(disk_map):
    idx = '.'
    if (i+1)%2: 
        idx = ID
        ID += 1
    if cell != '0':
        blocks +=[idx] * int(cell)

checksum1 = 0

# for i,b in enumerate(blocks):
#     if b == '.':
#         last = blocks.pop()
#         while last == '.':
#             last = blocks.pop()
#         blocks[i] = last
#     checksum1 += blocks[i] * i


# checksum1
# 6258319840548


checksum2 = 0

def find_empty_space(pos, length):
    for i,b in enumerate(blocks):
        if b == '.':
            if all([x=='.' for x in blocks[i:i+length]]):
                if i < pos:
                    return i
    return False

def get_bunch(id):
    pos = blocks.index(id)
    length = blocks.count(id)
    return (pos, length)


ID = blocks[-1]

for i in range(ID, -1, -1):
    pos, length = get_bunch(i)
    if new_pos := find_empty_space(pos, length):
        for p in range(length):
            blocks[new_pos+p] = blocks[pos+p]
            blocks[pos+p] = '.'
    
    

for i,b in enumerate(blocks):
    if b != '.':
        checksum2 += blocks[i] * i


# checksum2
# 6286182965311



























