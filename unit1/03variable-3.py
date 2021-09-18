

r = range(15)
print( r, '\n',type(r))
for i in r:
    print (i)
print('\n')


r2 = range(2,10)
print( r2, '\n',type(r2))
for i in r2:
    print (i)
print('\n')


r3 = range(1,20,2)
print( r3, '\n',type(r3))
for i in r3:
    print (i)
print('\n')


fruits = ['apple','banana','mango']
print(fruits, '\n',type(fruits))
print('\n')

for item in fruits:
    print (item)

fruits = fruits+fruits
print(fruits, '\n',type(fruits))
print('\n')


#r = r+r
#del r[0]
del r
#print(r)

del fruits[0]
print(fruits)

