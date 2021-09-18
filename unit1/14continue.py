
for i in range(10):
    if i % 2 == 0:
        continue
    print(' '*(9-i),'*'*(i+1),sep='')
print('_'*10)
