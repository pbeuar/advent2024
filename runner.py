

disk_map = '2333133121414131402'

# =================================================

# blocks = ''

# ID = 0

# for i, cell in enumerate(disk_map):
#     idx = '.'
#     if (i+1)%2: 
#         idx = str(ID)
#         ID += 1
#     blocks += int(cell) * idx

# 00...111...2...333.44.5555.6666.777.888899

# =================================================

blocks = []

ID = 0

for i, cell in enumerate(disk_map):
    idx = '.'
    if (i+1)%2: 
        idx = ID
        ID += 1
    if cell != '0':
        blocks += [idx] * int(cell)


blocks1 = []

ID = 0

for i, cell in enumerate(disk_map):
    idx = '.'
    if (i+1)%2: 
        idx = ID
        ID += 1
    if cell != '0':
        blocks1.append([idx] * int(cell))



checksum = 0

# for i,b in enumerate(blocks):
#     if b == '.':
#         last = blocks.pop()
#         while last == '.':
#             last = blocks.pop()
#         blocks[i] = last
#     checksum += blocks[i] * i



# 0099811188827773336446555566
# =========================================



# for r,rb in enumerate(reversed(blocks)):
#     for i,b in enumerate(blocks):
#         if rb[0] != '.' and b[0] == '.' and len(b) >= len(rb):
#             temp = rb
#             blocks.remove(rb)
#             blocks[i] = temp
#             # dif = len(b) - len(temp)
#             # if dif > 0:
#             #     blocks.insert(i+1, ['.']*dif)

#             # blocks[-1-r] = len(rb)*'.'

#             break
            
    
# for r in range(len(blocks)-1, -1, -1):
#     print(blocks[r])
#     for i,b in enumerate(blocks):
#         if b[0] == '.' and len(b) >= len(blocks[r]):
#             blocks[i] = blocks.pop(r)
#             dif = len(b) - len(blocks[1])
#             if dif > 0:
#                 print(dif)
#                 blocks.insert(i+1, ['.'] * dif)
#                 break
                
            



















        
























