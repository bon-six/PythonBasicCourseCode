

a=True
b=False
c=20.34567891
d=-12.3456789

s1='the bool data has 2 value: {0} and {1}'.format(a,b)
print(s1)
s2='the bool data has 2 value: {1} and {0}'.format(a,b)
print(s2)

s3 ='value of c is {: > .2f}'.format(c)
print(s3)

s4 ='value of c is {: > .2f}'.format(d)
print(s4)

s5 ='value of c is {: > .2e}'.format(c)
print(s5)

s6 ='value of c is {: > .2e}'.format(d)
print(s6)

s7=''
width = 9
for base in 'dXob':
    s7+='{0:{width}{base}}'.format(95,base=base,width=width)
print(s7)
