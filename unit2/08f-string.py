

name = 'Tom'
age = 7

rec_no = 0xbcaaaaaa


s1=f'{name} is {age} years old'
print(s1)

s2=f'Report to {name}, record no {rec_no:#x}'
print(s2)
s2=f'Report to {name}, record no {rec_no:#d}'
print(s2)
s2=f'Report to {name}, record no {rec_no:#o}'
print(s2)
s2=f'Report to {name}, record no {rec_no:#b}'
print(s2)

s3=f'here is the {name} * {age} and result is {name*age}'
print(s3)

s4=f'{name} is funny with {name.lower()}'
print(s4)

s5=f'{name} is funny with {name.upper()}'
print(s5)

