import hashlib

key = 'yzbqklnj'

i = 0

while True:
    istr = str(i)
    hashstr = key + istr
    result = hashlib.md5(hashstr.encode())
    rstr = result.hexdigest()
    if rstr[0:6] == '000000':
        break

    i = i + 1

print('part 1: ', i)


