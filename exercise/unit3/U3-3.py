
l1 = [[] for i in range(10)]

for i in range(10,20):
    for j in (2,3,5):
        if i%j == 0:
            l1[j].append(i)

for i in range(10):
    print(l1[i])
