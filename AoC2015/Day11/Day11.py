def incrementPW(pwd):
    i = len(pwd)-1

    pwd[i] = chr(ord(pwd[i]) + 1)

    while pwd[i] == '{':
        pwd[i] = 'a'
        i = i - 1
        pwd[i] = chr(ord(pwd[i]) + 1) 

def hasStraight(pwd):
    for i in range(len(pwd)-2):
        c0 = ord(pwd[i])
        c1 = ord(pwd[i+1])
        c2 = ord(pwd[i+2])
        if c2 == c1+1 and c1 == c0+1:
            return True

    return False

def hasForbidden(pwd):
    forbidden = ['i', 'o', 'l']

    for f in forbidden:
        if f in pwd:
            return True

    return False

def findPair(pwd):
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            return i+2

    return None

def hasTwoPair(pwd):

    i = findPair(pwd)
    if i != None:
        j = findPair(pwd[i:])
        if j != None:
            return True
    return False

pwd = 'hepxcrrq'
pwd = list(pwd)


while True:
    incrementPW(pwd)

    if hasTwoPair(pwd) and hasStraight(pwd) and not hasForbidden(pwd):
        break

print(pwd)

while True:
    incrementPW(pwd)

    if hasTwoPair(pwd) and hasStraight(pwd) and not hasForbidden(pwd):
        break

print(pwd)