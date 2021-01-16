with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

auntList = []

for line in text_input:

    name, fields = line.strip().split(':', 1)
    f1, f2, f3 = fields.strip().split(', ')
    f1n, f1v = f1.split(': ')
    f2n, f2v = f2.split(': ')
    f3n, f3v = f3.split(': ')

    f1v = int(f1v)
    f2v = int(f2v)
    f3v = int(f3v)
    auntList.append({})
    auntList[-1]['name'] = name
    auntList[-1][f1n] = f1v
    auntList[-1][f2n] = f2v
    auntList[-1][f3n] = f3v


mfcsam = {}
mfcsam['children'] = 3
mfcsam['cats'] = 7
mfcsam['samoyeds'] = 2
mfcsam['pomeranians'] = 3
mfcsam['akitas'] = 0
mfcsam['vizslas'] = 0
mfcsam['goldfish'] = 5
mfcsam['trees'] = 3
mfcsam['cars'] = 2
mfcsam['perfumes'] = 1


for sue in auntList:
    bFound = True
    for k in sue.keys():
        if k == 'name':
            pass
        else:
            if mfcsam[k] != sue[k]:
                bFound = False

    if bFound:
        print('Part 1: ', sue['name'], ' sent us the MFCSAM!')
        break

# part 2

for sue in auntList:
    bFound = True
    for k in sue.keys():
        if k == 'name':
            pass
        elif k in ['cats', 'trees']:
            if mfcsam[k] >= sue[k]:
                bFound = False
        elif k in ['pomeranians', 'goldfish']:
            if mfcsam[k] <= sue[k]:
                bFound = False
        else:
            if mfcsam[k] != sue[k]:
                bFound = False

    if bFound:
        print('Part 2: ', sue['name'], ' sent us the MFCSAM!')
        break



