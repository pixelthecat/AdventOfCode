
with open('puzzleinput.txt', 'r') as f:
    text_input = f.readlines()

f.close()

numStringLit = 0
numStringVal = 0
numStringLong = 0

# escaped characters: \\, \" and \x.., plus ignore surrounding "


for line in text_input:
    line = line.strip()
    numStringLit += len(line)
    numStringLong += len(line) + 4 # include the expansion of the quotes

    i = 1             # skip the first quote
    while i < len(line)-1:            #also skip the last quote
        if line[i] == '\\':
            if line[i+1] == '\\' or line[i+1] == '\"':
                i += 2
                numStringLong += 2
            elif line[i+1] == 'x':
                i += 4
                numStringLong += 1
        else:
            i += 1

        numStringVal += 1




print('Part 1: ', numStringLit, numStringVal, numStringLit - numStringVal)
print('Part 2: ', numStringLit, numStringVal, numStringLong - numStringLit)