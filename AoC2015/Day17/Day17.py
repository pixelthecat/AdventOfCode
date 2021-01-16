from itertools import combinations 


with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()


containerList = []

for line in text_input:
    line = line.strip()
    containerList.append(int(line))

containerList.sort()

totalVol = 150

# find the max number of containers 

i = 0
vol = 0

while vol < totalVol:
    vol += containerList[i]
    i += 1

maxNum = i-1

numContainerCombos = 0
minNumCont = maxNum + 4

for r in range(maxNum+1):
    for c in combinations(containerList, r):
        if sum(c) == totalVol:
            numContainerCombos += 1
            minNumCont = min(minNumCont, len(c))

print('Part 1: ', numContainerCombos)

numContainerCombos = 0

for c in combinations(containerList, minNumCont):
    if sum(c) == totalVol:
        numContainerCombos += 1

print('Part 2: ', numContainerCombos)