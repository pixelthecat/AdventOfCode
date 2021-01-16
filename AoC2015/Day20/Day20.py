import math

def findDivisors(num):
    divs = set()

    i = 1
    sn = int(math.ceil(math.sqrt(num)))

    while i <= sn: 
          
        if (num % i == 0) :               
            divs.add(i)
            divs.add(num//i)
                
        i = i + 1

    return divs


def numPressiesAtHouse(hnum):
    numpressies = 0

    divs = findDivisors(hnum)
    numpressies = sum(divs)*10
    return numpressies

def numPressiesAtHousePart2(hnum):
    numpressies = 0

    divs = findDivisors(hnum)
    for d in divs:
        if (hnum // d) <= 50:
            numpressies += d*11

    return numpressies

myNum = 36000000



# i = 1

# while numPressiesAtHouse(i) <= myNum:
#    i += 1

# print('Part 1: ', i)

i = 1

while numPressiesAtHousePart2(i) <= myNum:
    i += 1

print('Part 2: ', i)
