

with open('input') as f:
    data = f.read()
    

data1, data2 = data.split("\n\n")

rules = [[int(y) for y in x.split('|')] for x in data1.split()]

lines = [[int(y) for y in x.split(',')] for x in data2.split()]


def check_rule(rule, line):
    a, b = rule
    if a in line and b in line:        
        return line.index(a) < line.index(b)
    return True

def check_line(line):
    ok = True
    for rule in rules:
        if ok:
            ok =  check_rule(rule, line)
    return ok

good_lines = []
bad_lines = []
answer = 0 #7307
answer2 = 0 #4713

for line in lines:
    if check_line(line):
        good_lines.append(line)
        answer += line[len(line)//2]
    else:
        bad_lines.append(line)
        
        
def apply_rule(rule,line):
    a, b = rule
    if a in line and b in line:
        a_idx = line.index(a)
        b_idx = line.index(b)
        if a_idx > b_idx:
            line[b_idx], line[a_idx] = line[a_idx], line[b_idx]


for line in bad_lines:
    while not check_line(line):
        for rule in rules:
            apply_rule(rule, line)
    
    answer2 += line[len(line)//2]
    
    

            
    
