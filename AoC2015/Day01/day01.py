with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

floor = 0

line = text_input[0].strip()
instr = None
for i, c in enumerate(line):
    if c == '(':
        floor = floor + 1
    elif c == ')':
        floor = floor - 1
    if instr == None and floor == -1:
        instr = i

print('Part 1: floor is ', floor)
print('Part 2: instr is ', instr+1)