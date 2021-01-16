def nextValue(prevValue):
    nv = prevValue * 252533
    nv = nv % 33554393
    return nv



# To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083.


r = 1
c = 1
startrow = 1

code = 20151125


while True:
    if r == 1:
        c = 1
        startrow = startrow + 1
        r = startrow
    else:
        c += 1
        r -= 1

    code = nextValue(code)
    if r == 2978 and c == 3083:
        break

print('Part 1: ', code)
