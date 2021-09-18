
i = 16

s = '16'

#n = s + i
#n = i + s

n1 = int(s) + i
print(n1, '\n', type(n1))
print('\n')

s1 = str(i) + s
print(s1, '\n', type(s1))
print('\n')

s2 = '16xy'
#n2 = int(s2) + i

s3 = '16.32'
#n3 = int(s3) + i

n4 = float(s3) + i
print( n4, '\n',  type(n4))
print('\n')
    
n5 = int(float(s3)) + i
print(n5, '\n', type(n5))
print('\n')
