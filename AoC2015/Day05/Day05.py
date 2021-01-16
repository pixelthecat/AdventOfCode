def hasTwoPair(str):

    for i in range(len(str)-3):
        m = str[i]+str[i+1]
        if str.count(m) > 1:
            return True
    return False

def hasRepeatSpace(str):

    for i in range(len(str)-2):
        if str[i]==str[i+2]:
            return True

    return False

def numVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']

    n = 0

    for v in vowels:
        n = n + str.count(v)

    return n

def hasDoubleLetters(str):

    for c in str:
        if c+c in str:
            return True
    return False

def hasNaughtyBits(str):
    naughtyBits = ['ab', 'cd', 'pq', 'xy']

    for nb in naughtyBits:
        if nb in str:
            return True
    
    return False

with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

numNice = 0

for line in text_input:
    line = line.strip()

    nice = numVowels(line) > 2 
    nice = nice and hasDoubleLetters(line)
    nice = nice and not hasNaughtyBits(line)
    if nice:
        numNice += 1

print('Part 1: there are ', numNice, ' nice strings')

numNice = 0
for line in text_input:
    line = line.strip()

    nice = hasTwoPair(line) 
    nice = nice and hasRepeatSpace(line)
    if nice:
        numNice += 1
print('Part 2: there are ', numNice, ' nice strings')
