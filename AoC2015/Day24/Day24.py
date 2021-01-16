from itertools import combinations

def subset_sum(numbers, target, masterlist, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
#        print("sum(%s)=%s" % (partial, target))
        masterlist.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, masterlist, partial + [n])

def subsetsum_exists(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        return True
    if s >= target:
        return False # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        rval = subsetsum_exists(remaining, target, partial + [n])
        if rval:
            return True

def subsetsum_minsize(numbers, target):
    grouplist = []

    for n in range(1,len(numbers)):
        combs = combinations(numbers, n)
        for c in combs:
            if sum(c) == target:
                grouplist.append(c)

        if len(grouplist) > 0:
            return grouplist

    return []


def qe(group):
    p = 1

    for g in group:
        p = p * g

    return p

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

pressiepile = set()

for line in text_input:
    line = line.strip()
    pressiepile.add(int(line))


grouplist = []
groupWeight = sum(pressiepile)//4

# subset_sum(list(pressiepile), groupWeight, grouplist)
#minlen = len(grouplist[0])

#for f in grouplist:
#    minlen = min(minlen, len(f))

#groupAList = []

#for f in grouplist:
#    if len(f) == minlen:
#        groupAList.append(f)

groupAList = subsetsum_minsize(list(pressiepile), groupWeight)


minQE = qe(pressiepile)

qelist = []

for groupA in groupAList:
    qelist.append((qe(groupA), groupA))

qelist.sort()

for q in qelist:
    groupA = q[1]

    tmp = pressiepile.copy()
    tmp.difference_update(groupA)

    if subsetsum_exists(list(tmp),groupWeight):
        print('Part 2: ', q[0])
        break


#    tmp = pressiepile.copy()
#    tmp.difference_update(groupA)
#    tmplist = []
#    subset_sum(list(tmp), groupWeight, tmplist)
#    if len(tmplist) > 0:
#        minQE = min(minQE, qe(groupA))


