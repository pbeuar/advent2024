

with open('input') as f:
    data = [line.strip() for line in f]

width = len(data[0])
height = len(data)

word = 'XMAS'

dirs = [(0,1),        
        (1,0),
        (1,1),
        (0,-1),
        (-1,0),
        (-1,-1),
        (-1,1),
        (1,-1)]

def check_dir(w,h,d,l):
    a = w+d[0]
    b = h+d[1]
    if a >= 0 and a < width and b >= 0 and b < height:
        if data[a][b] == l:
            return a,b
    return False
    

count = 0

for w in range(width):
    for h in range(height):
        if data[w][h]==word[0]:
            for dir in dirs:                
                if check_dir(w, h, dir, word[1]):
                    a,b = check_dir(w, h, dir, word[1])                    
                    if check_dir(a, b, dir, word[2]):
                        a,b = check_dir(a, b, dir, word[2])
                        if check_dir(a, b, dir, word[3]):
                            count += 1

answer1 = count
# 2613


count2 = 0

xdirs = [[(1,1), (-1,-1)],
         [(-1,1), (1,-1)]]

def add_dir(w,h,d):
    return data[w+d[0]][h+d[1]]
                            
def check_x(w,h):
    options =  [[add_dir(w, h, d) for d in x] for x in xdirs]
    for opt in options:
        for i in 'MS':
            if not i in opt:
                return False
    return True


for w in range(1,width-1):
    for h in range(1, height-1):
        if data[w][h] == 'A':
            if check_x(w,h):
                count2 += 1
            

answer2 = count2
# 1905



# with walrus:
    
    
# for w in range(width):
#     for h in range(height):
#         if data[w][h]==word[0]:
#             for dir in dirs:                
#                 if (ab := check_dir(w, h, dir, word[1])):                 
#                     if (cd := check_dir(ab[0], ab[1], dir, word[2])):
#                         if check_dir(cd[0], cd[1], dir, word[3]):
#                             count += 1

