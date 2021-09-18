
i1=0
i2=1
print (i1)
print(i2)

for j in range(20):
    i3 = i1+i2
    i1 = i2
    i2 = i3
    print (i3)
    if (i3>100):
        break
print('end!')
