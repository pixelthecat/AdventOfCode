def toggleField(field, startx, starty, endx, endy):

    for y in range(starty, endy+1):
        for x in range(startx, endx+1):
            field[y][x] = not field[y][x]
 
def setField(field, startx, starty, endx, endy, val):
    for y in range(starty, endy+1):
        for x in range(startx, endx+1):
            field[y][x] = val

def toggleFieldP2(field, startx, starty, endx, endy):

    for y in range(starty, endy+1):
        for x in range(startx, endx+1):
            field[y][x] = field[y][x]+2
 
def setFieldP2(field, startx, starty, endx, endy, val):
    if val:
        inc = 1
    else:
        inc = -1

    for y in range(starty, endy+1):
        for x in range(startx, endx+1):
            field[y][x] = max(field[y][x]+inc, 0)

def getCoords(str):
    x,y = str.split(',')
    x = int(x)
    y = int(y)

    return x,y


with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

field = []

for i in range(1000):
    field.append([False]*1000)

for line in text_input:
    line = line.strip()

    linesplt = line.split(' ')
    if len(linesplt) == 4:
        # contains toggle
        startstr = linesplt[1]
        endstr = linesplt[3]
        startx, starty = getCoords(startstr)
        endx, endy = getCoords(endstr)
        toggleField(field, startx, starty, endx, endy)
    else:
        # contains turn on or off
        startstr = linesplt[2]
        endstr = linesplt[4]
        startx, starty = getCoords(startstr)
        endx, endy = getCoords(endstr)
        val = linesplt[1] == 'on'
        setField(field, startx, starty, endx, endy, val)

numOn = 0

for row in field:
    for c in row:
        if c:
            numOn = numOn + 1

print('part 1: ', numOn)    

field = []

for i in range(1000):
    field.append([0]*1000)

for line in text_input:
    line = line.strip()

    linesplt = line.split(' ')
    if len(linesplt) == 4:
        # contains toggle
        startstr = linesplt[1]
        endstr = linesplt[3]
        startx, starty = getCoords(startstr)
        endx, endy = getCoords(endstr)
        toggleFieldP2(field, startx, starty, endx, endy)
    else:
        # contains turn on or off
        startstr = linesplt[2]
        endstr = linesplt[4]
        startx, starty = getCoords(startstr)
        endx, endy = getCoords(endstr)
        val = linesplt[1] == 'on'
        setFieldP2(field, startx, starty, endx, endy, val)

brightness = 0
for row in field:
    brightness += sum(row)

print('Part 2: There are ', brightness, ' brightnessess')