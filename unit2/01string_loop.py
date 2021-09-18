

s1 = 'This is a string.'

print('str 1 is', s1, '\n', 'has', len(s1), 'characters')

for i in range(len(s1)):
    print (s1[i])
print('----End!')


for c in s1:
    print(c)
print(type(c))
print('****End!')

print('\n')
s2 = "in double quote' "
s3 = 'in single quote". '
s4 = ''' a triple quote string,
can have 'multiple" lines.
    again one more line'''

print (s2)
print('\n')
print(s3)
print()
print(s4)
