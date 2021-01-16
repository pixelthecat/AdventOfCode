def stringToList(str):
    lst=[] 
    lst[:0]=str 
    return lst 

def listToString(s):  
    # initialize an empty string 
    str = '' 
    
    # return string   
    return (str.join(s))

def findPositions(med, src):
    posList = []

    i = 0
    
    for i in range(len(med)+1-len(src)):
        if med[i:i+len(src)] == src:
            posList.append(i)
    
    return posList

def makeNewMolecule(med, src, trg):
    
    posList = findPositions(med, src)

    for p in posList:
        
        if p == 0:
            medListTmp = med.replace(src, trg, 1)
        else:
            medListTmp = med[:p] + med[p:].replace(src, trg, 1)

        yield medListTmp

    


with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

recipies = {}
rev_recipies = {}

for line in text_input:
    line = line.strip()
    if '=>' in line:
        # recipe
        mol, sub = line.split(' => ')
        mollist = recipies.setdefault(mol, [])
        mollist.append(sub)
        
        rev_recipies[sub] = mol

    elif line == '\n':
        pass
    else:
        # medicine molecule
        med = line

medSet = set()

for k in recipies.keys():
    for n in recipies[k]:
        for mol in makeNewMolecule(med, k, n):
            medSet.add(mol)

print('part 1: ', len(medSet))

# now part 2: start with e, get to the medicine molecule and count steps
# or, go backwards to e

mol = med
steps = 0

while mol != 'e':
    steps += 1
    for k in rev_recipies.keys():
        if k in mol:
            mol = mol.replace(k, rev_recipies[k], 1)
            print(mol)
            break


print('Part 2: ', steps)