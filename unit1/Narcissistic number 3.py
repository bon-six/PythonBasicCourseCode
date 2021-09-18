
for i in range (100,1000):
    d3 = i%10
    d2 = (i//10)%10
    d1 = i//100
    if i == d1**3 + d2**3 + d3**3:
        print(i)
print('End!')
