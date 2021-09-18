

i = 100

while i<1000:
    a = i//100
    b = i//10 - i//100*10
    c = i - i//10*10
    if i == a**3 + b**3 + c**3:
        print(i)
    i += 1
print('End!')
