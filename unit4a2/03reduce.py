

import functools

l1 = [1,2,3,4,5,6,7,8,9]

result = functools.reduce(lambda x1, x2: x1+x2, l1)

print(result)



fac = lambda n : functools.reduce(lambda x1, x2: x1*x2, range(1,n+1))

print(fac(3))
print(fac(5))
