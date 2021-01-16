num = [1,1,1,3,1,2,2,1,1,3]

newNum = []

for n in range(50):
    currD = num[0]
    currCtr = 1
#    print('iteration ', n, ': ', num)
    newNum = []
    for i in range(1, len(num)):
        d = num[i]

        if d == currD:
            currCtr += 1
        else:
            newNum.append(currCtr)
            newNum.append(currD)
            currD = d
            currCtr = 1

    newNum.append(currCtr)
    newNum.append(currD)
    num = newNum

print('part 1: ', len(num))