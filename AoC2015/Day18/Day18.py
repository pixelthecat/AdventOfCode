def numNeighborsTrue(field, xy):
    numTrue = 0
    x = xy[0]
    y = xy[1]

    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if field.get((i,j), False):
                numTrue += 1
    if field[xy]:
        numTrue -= 1

    return numTrue

def printField(field, lenX, lenY):

    for j in range(lenY):
        for i in range(lenX):
            if field[(i,j)]:
                c = '#'
            else:
                c = '.'
            print(c, end='')
        print('')

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()


field = {}
lenY = 0

for j, line in enumerate(text_input):
    lenY += 1
    line = line.strip()
    lenX = len(line)
    for i, c in enumerate(line):
        field[(i,j)] = (c=='#')

numIters = 100

corners = [(0,0), (0,lenY-1), (lenX-1, 0), (lenX-1, lenY-1)]
for k in corners:
    field[k] = True

for n in range(numIters):
    newField = field.copy()

    for k in field.keys():
        nn = numNeighborsTrue(field,k)
        if field[k]:
            if nn not in [2,3]:
                newField[k] = False
        else:
            if nn == 3:
                newField[k] = True

    for k in corners:
        newField[k] = True

    field = newField

numOn = list(field.values()).count(True)

print('Part 1: ', numOn)