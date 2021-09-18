i = 100

while i<1000:
    str_i = str(i)
    power = len(str_i)
    total = 0
    for digit in str_i:
        total += int(digit)**power
    if total == i:
        print (i)
    i += 1
print('End!')
