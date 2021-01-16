with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

boxList = []

for line in text_input:
    line = line.strip()
    x,y,z = line.split('x')
    boxList.append((int(x),int(y),int(z)))

totalArea = 0
totalRibbon = 0


for box in boxList:
    a1 = box[0]*box[1]
    a2 = box[0]*box[2]
    a3 = box[1]*box[2]
    area = a1*2 + a2*2 + a3*2 + min([a1, a2, a3])
    totalArea = totalArea + area

    sideList = list(box)
    r1 = min(sideList)
    sideList.remove(r1)
    r2 = min(sideList)
    rlen = 2*r1 + 2*r2 + box[0]*box[1]*box[2]
    totalRibbon = totalRibbon + rlen

print('Part 1: area is ', totalArea)
print('Part 2: need ', totalRibbon, ' feet of ribbon')