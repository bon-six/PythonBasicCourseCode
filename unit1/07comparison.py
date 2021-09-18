

i = 17

f = 17.6

b = i < f
print(b, '\n', type(b))
print('\n')

b2 = i < int(f)
print(b2, '\n', type(b2))
print('\n')

b3 = i <= int(f)
print(b3, '\n', type(b3))
print('\n')

s = 'abc'
s2 = 'ABC'
b4 = s<s2
print(b4, '\n', type(b4))
print('\n')

s3 = 'acd'
b5 = s<s3
print(b5, '\n', type(b5))
print('\n')

#b6 = i < s

b7 = str(i) < s
print(b7, '\n', type(b7))
print('\n')

b8 = str(i) < s2
print(b8, '\n', type(b8))
print('\n')
