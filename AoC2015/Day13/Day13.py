from itertools import permutations

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()


# Alice would gain 54 happiness units by sitting next to Bob.

guests = {}
guestSet = set()

for line in text_input:
    words = line.strip().strip('.').split()
    name1 = words[0]
    name2 = words[-1]
    gain = (words[2] == 'gain')
    num = int(words[3])
    guestSet.add(name1)
    if name1 not in guests.keys():
        guests[name1] = {}
    if not gain:
        num = -num

    guests[name1][name2] = num

perms = permutations(guestSet)

maxHappiness = 0

for p in perms:
    happy = 0
    for i in range(len(guestSet)):
        before = p[(i-1)%len(guestSet)]
        after = p[(i+1)%len(guestSet)]
        happy += guests[p[i]][before] + guests[p[i]][after]
    maxHappiness = max(maxHappiness, happy)

    
print('Part 1: ', maxHappiness)

myName = 'Rasputin'
guestSet.add(myName)
guests[myName] = {}
for k in guests.keys():
    guests[k][myName] = 0
    guests[myName][k] = 0

perms = permutations(guestSet)

maxHappiness = 0

for p in perms:
    happy = 0
    for i in range(len(guestSet)):
        before = p[(i-1)%len(guestSet)]
        after = p[(i+1)%len(guestSet)]
        happy += guests[p[i]][before] + guests[p[i]][after]
    maxHappiness = max(maxHappiness, happy)

    
print('Part 2: ', maxHappiness)

