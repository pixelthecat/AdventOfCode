import collections
import itertools


Item = collections.namedtuple('Item', ['name', 'dmg', 'ac', 'cost'])

def simulateBattle(p, b):
    # 
    pHP = p['hp']
    bHP = b['hp']

    playerDPT = max(1, p['weapon'].dmg + p['ring1'].dmg + p['ring2'].dmg - b['ac'])
    bossDPT = max(1, b['dmg'] - p['ring1'].ac - p['ring2'].ac - p['armor'].ac)

    while True:
        # player attack boss
        bHP -= playerDPT
        if bHP <= 0:
            return True

        # boss attack player
        pHP -= bossDPT
        if pHP <= 0:
            return False


weapons = []
weapons.append(Item(name='dagger',       dmg=4, ac=0, cost=8))
weapons.append(Item(name='shortsword',   dmg=5, ac=0, cost=10))
weapons.append(Item(name='warhammer',    dmg=6, ac=0, cost=25))
weapons.append(Item(name='longsword',    dmg=7, ac=0, cost=40))
weapons.append(Item(name='greataxe',     dmg=8, ac=0, cost=74))

armors = []
armors.append(Item(name='yfronts',       dmg=0, ac=0, cost=0))
armors.append(Item(name='leather',       dmg=0, ac=1, cost=13))
armors.append(Item(name='chainmail',     dmg=0, ac=2, cost=31))
armors.append(Item(name='splintmail',    dmg=0, ac=3, cost=53))
armors.append(Item(name='bandedmail',    dmg=0, ac=4, cost=75))
armors.append(Item(name='platemail',     dmg=0, ac=5, cost=102))

rings = []
rings.append(Item(name='gaudyring',      dmg=0, ac=0, cost=0))
rings.append(Item(name='pulltab',        dmg=0, ac=0, cost=0))
rings.append(Item(name='damage +1',      dmg=1, ac=0, cost=25))
rings.append(Item(name='damage +2',      dmg=2, ac=0, cost=50))
rings.append(Item(name='damage +3',      dmg=3, ac=0, cost=100))
rings.append(Item(name='defense +1',     dmg=0, ac=1, cost=20))
rings.append(Item(name='defense +2',     dmg=0, ac=2, cost=40))
rings.append(Item(name='defense +3',     dmg=0, ac=3, cost=80))

boss = {}
boss['ac'] = 2
boss['dmg'] = 9
boss['hp'] = 102

player = {}
player['hp'] = 100

minCost = 74+102+100+80+1        # this more than the most we could spend



for w in weapons:
    player['weapon'] = w
    for a in armors:
        player['armor'] = a
        
        ringComb = itertools.combinations(rings, 2)
        for rc in ringComb:
           cost = w.cost + a.cost + rc[0].cost + rc[1].cost
           player['ring1'] = rc[0]
           player['ring2'] = rc[1]
#           print('checking with ', player['weapon'].name, ', ', player['armor'].name, ', ', player['ring1'].name, ', ', player['ring2'].name, '. Cost: ', cost)
           if cost < minCost:
              
               if simulateBattle(player, boss):
                   print('player won with ', player['weapon'].name, ', ', player['armor'].name, ', ', player['ring1'].name, ', ', player['ring2'].name, '. Cost: ', cost)
                   minCost = cost

print('Part 1: ', minCost)

maxCost = 0

for w in weapons:
    player['weapon'] = w
    for a in armors:
        player['armor'] = a
        
        ringComb = itertools.combinations(rings, 2)
        for rc in ringComb:
           cost = w.cost + a.cost + rc[0].cost + rc[1].cost
           player['ring1'] = rc[0]
           player['ring2'] = rc[1]
#           print('checking with ', player['weapon'].name, ', ', player['armor'].name, ', ', player['ring1'].name, ', ', player['ring2'].name, '. Cost: ', cost)
           if cost > maxCost:
              
               if simulateBattle(player, boss) == False:
                   print('player lost with ', player['weapon'].name, ', ', player['armor'].name, ', ', player['ring1'].name, ', ', player['ring2'].name, '. Cost: ', cost)
                   maxCost = cost

print('Part 2: ', maxCost)