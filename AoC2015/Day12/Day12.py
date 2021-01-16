import json
import copy

def totalFromList(mylist):
    tot = 0

    for x in mylist:
        if isinstance(x, int):
            tot += x
        elif isinstance(x, list):
            tot += totalFromList(x)
        elif isinstance(x, dict):
            tot += totalFromDict(x)

    return tot

def totalFromDict(myd):
    
    tot = 0

    if 'red' in myd.keys() or 'red' in myd.values():
        return 0

    for k in myd.keys():
        if isinstance(k, int):
            tot += k

    for v in myd.values():
        if isinstance(v, int):
            tot += v
        elif isinstance(v, list):
            tot += totalFromList(v)
        elif isinstance(v, dict):
            tot += totalFromDict(v)

    return tot

                



with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

replDict = {}

p1Total = 0

p2line = copy.copy(text_input[0])

for line in text_input:
    for c in line:
        if c.isdigit() == False and c != '-':
            replDict[c] = ' '
    mytable = line.maketrans(replDict)
    newLine = line.translate(mytable)
    
    for nums in newLine.split():
        num = int(nums)
#        print(num)
        p1Total += num


print('Part 1: ', p1Total)

mydict = json.loads(p2line)

print('Part 2: ', totalFromDict(mydict))