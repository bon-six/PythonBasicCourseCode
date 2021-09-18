tri = [[0 for i in range(0,9)] for j in range(0, 9)]

for i in range(0, 9):
    print('  '*(10-i),sep='', end='')
    for j in range(0,i+1):
        if i == 0 or j == 0 or i == j:
            tri[i][j] = 1
        else:
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
        print(f'{tri[i][j]:4d}',sep='', end='')
    print()
        

