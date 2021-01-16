import collections
import itertools

import itertools

# from https://stackoverflow.com/questions/28965734/general-bars-and-stars
def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()



Ingredient = collections.namedtuple('Ingredient', ['name', 'cap', 'dur', 'fla', 'tex', 'cal'])

ingredients = []

for line in text_input:
    # Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
    #   0           1     2    3        4    5     6    7     8    9      10
    words = line.strip().split()
    name = words[0].strip(':')
    cap = int(words[2].strip(','))
    dur = int(words[4].strip(','))
    fla = int(words[6].strip(','))
    tex = int(words[8].strip(','))
    cal = int(words[10].strip())

    ingredients.append(Ingredient(name, cap, dur, fla, tex, cal))


maxTsp = 100
bestScore = 0
bestScore500 = 0

for p in partitions(100, len(ingredients)):
    tCap = 0
    tDur = 0
    tFla = 0
    tTex = 0
    tCal = 0

    for i, ing in enumerate(ingredients):
        tCap += ing.cap*p[i]
        tDur += ing.dur*p[i]
        tFla += ing.fla*p[i]
        tTex += ing.tex*p[i]
        tCal += ing.cal*p[i]
    tCap = max(0, tCap)
    tDur = max(0, tDur)
    tFla = max(0, tFla)
    tTex = max(0, tTex)

    score = tCap * tDur * tFla * tTex
    bestScore = max(score, bestScore)
    if tCal == 500:
        bestScore500 = max(score, bestScore500)


print('Part 1: ', bestScore)
print('Part 2: ', bestScore500)