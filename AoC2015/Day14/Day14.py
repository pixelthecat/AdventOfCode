import collections

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

Reindeer = collections.namedtuple('Reindeer', ['name', 'speed', 'goSecs', 'restSecs', 'cycle'])

reindeerList = []

#    0    1   2   3  4    5  6    7      8    9   10    11  12  13
# Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.

for line in text_input:
    words = line.strip().split()
    name = words[0]
    speed = int(words[3])
    goSecs = int(words[6])
    restSecs = int(words[13])
    cycle = goSecs + restSecs
    reindeerList.append(Reindeer(name, speed, goSecs, restSecs, cycle))

totalSecs = 2503

maxDist = 0

for r in reindeerList:
    cycles = totalSecs // r.cycle
    remainder = totalSecs % r.cycle
    remainder = min(remainder, r.goSecs)
    dist = r.speed*(r.goSecs * cycles + remainder)
    maxDist = max(maxDist, dist)
    print(r.name,' has gone ', dist, ' km. cycles: ', cycles, ' remainder: ', remainder)

print('Part 1: ', maxDist)

reindeerDist = [0]*len(reindeerList)
reindeerScore = [0]*len(reindeerList)

for t in range(totalSecs):
    cycleMaxDist = 0

    for i,r in enumerate(reindeerList):

        if (t % r.cycle) < r.goSecs:
            reindeerDist[i] += r.speed

    cycleMaxDist = max(reindeerDist)

    # gotta handle ties by going through a second time
    for i in range(len(reindeerList)):
        if reindeerDist[i] == cycleMaxDist:
            reindeerScore[i] += 1

print('Part 2: ', max(reindeerScore))

        
