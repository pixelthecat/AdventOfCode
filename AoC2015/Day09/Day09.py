from itertools import permutations

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()


cities = {}
cityNames = set()

maxDist = 0

for line in text_input:
    c, dist = line.strip().split(' = ')
    dist = int(dist)
    c1, c2 = c.split(' to ')
    cityNames.add(c1)
    cityNames.add(c2)

    if c1 not in cities:
        cities[c1] = {}
    cities[c1][c2] = dist

    if c2 not in cities:
        cities[c2] = {}
    cities[c2][c1] = dist
    maxDist += dist

minTrip = maxDist
maxTrip = 0
perms = permutations(cityNames)



for p in perms:
    d = 0
    for i in range(len(p)-1):
        d += cities[p[i]][p[i+1]]

    print(p, d)

    if d < minTrip:
        minTrip = d
    if d > maxTrip:
        maxTrip = d

print('part 1: min dist is ', minTrip)
print('part 2: max dist is ', maxTrip)
