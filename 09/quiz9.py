
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

for i,b in enumerate(blocks):
    if b == '.':
        last = blocks.pop()
        while last == '.':
            last = blocks.pop()
        blocks[i] = last
    checksum1 += blocks[i] * i


# checksum1
# 6258319840548


blocks1 = []

ID = 0

for i, cell in enumerate(disk_map):
    idx = '.'
    if (i+1)%2: 
        idx = ID
        ID += 1
    if cell != '0':
        blocks1.append([idx] * int(cell))

checksum2 = 0

# for i,b in enumerate(blocks):
#     if b == '.':
#         last = blocks.pop()
#         while last == '.':
#             last = blocks.pop()
#         blocks[i] = last
#     checksum2 += blocks[i] * i


        
























