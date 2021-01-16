def updatePosition(curPos, c):
    if c == '^':
        # go north - increment y
        curPos['y'] += 1
    elif c == '>':
        # go east - increment x
        curPos['x'] += 1
    elif c == 'v':
        # go south
        curPos['y'] -= 1
    elif c == '<':
        # go west
        curPos['x'] -= 1
    else:
        print('bad char ', c)

    cpos = (curPos['x'], curPos['y'])
    return cpos

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()


curPos = {'x': 0, 'y': 0}
visitedHouses = {}
visitedHouses[(curPos['x'], curPos['y'])] = 1

for line in text_input:
    line = line.strip()

    for c in line:
        if c == '^':
            # go north - increment y
            curPos['y'] += 1
        elif c == '>':
            # go east - increment x
            curPos['x'] += 1
        elif c == 'v':
            # go south
            curPos['y'] -= 1
        elif c == '<':
            # go west
            curPos['x'] -= 1
        else:
            print('bad char ', c)

        cpos = (curPos['x'], curPos['y'])
#        print(c, cpos)
        n = visitedHouses.setdefault(cpos, 0)
        n = n + 1
        visitedHouses[cpos] = n


print('Part 1: Santa visited ', len(visitedHouses), ' houses')

curPos = {'x': 0, 'y': 0}
curPosRS = {'x': 0, 'y': 0}

visitedHouses = {}
visitedHouses[(curPos['x'], curPos['y'])] = 2

for line in text_input:
    for i,c in enumerate(line.strip()):
        if i%2 == 0:
            # real santa
            cpos = updatePosition(curPos, c)
        else:
            cpos = updatePosition(curPosRS, c)
        n = visitedHouses.setdefault(cpos, 0)
        n = n + 1
        visitedHouses[cpos] = n

print('Part 2: Santas visited ', len(visitedHouses), ' houses')
