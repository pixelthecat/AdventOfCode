def resolveEntry(wd, entry):
    op = wd[entry][0]

    if op == 'VAL':
        # hurray!
        r = wd[entry][1]
    elif op == 'COPY':
        r = resolveEntry(wd, wd[entry][1])
    elif op == 'NOT':
        r = ~resolveEntry(wd, wd[entry][1])
    elif op == 'AND':
        p1 = wd[entry][1]
        p2 = wd[entry][2]
        r = resolveEntry(wd, p1) & resolveEntry(wd, p2)
    elif op == 'OR':
        p1 = wd[entry][1]
        p2 = wd[entry][2]
        r = resolveEntry(wd, p1) | resolveEntry(wd, p2)
    elif op == 'LSHIFT':
        p1 = wd[entry][1]
        p2 = int(wd[entry][2])
        r = resolveEntry(wd, p1) << p2
    elif op == 'RSHIFT':
        p1 = wd[entry][1]
        p2 = int(wd[entry][2])
        r = resolveEntry(wd, p1) >> p2
    else:
        print('we shouldnt be here! Nooooo!')

#    print(entry, ': ', r)
    wd[entry] = ['VAL', r & 0xFFFF]

    return r & 0xFFFF   

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

wd = {}


for line in text_input:
    line = line.strip()
    ops, dest = line.split(' -> ')
    
    if ops.isdigit():
        n = int(ops.strip())
        wd[dest] = ['VAL', n]
    else:
        # there's at least two elements, so not a number
        if 'NOT' in ops:
            # this is a NOT instruction
            instr, p1 = ops.strip().split(' ')
            wd[dest] = [instr, p1]
        elif len(ops.strip().split(' ')) > 1:
            p1, instr, p2 = ops.strip().split(' ')
            if p1.isdigit():
                wd[p1] = ['VAL', int(p1)]

            wd[dest] = [instr, p1, p2]
        else:
            instr = 'COPY'
            p1 = ops.strip()
            wd[dest] = [instr, p1]


wd['b'] = ['VAL', 956]

print('part 1: a : ', resolveEntry(wd, 'a'))

