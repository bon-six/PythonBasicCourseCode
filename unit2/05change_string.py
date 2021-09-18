

str_a = 'This is a string.'

str_b = '    Yet another string. ^_^     '

str_c = str_a.upper()
print(str_c)

str_d = str_a.lower()
print(str_d)

str_e = str_a.replace('s', 'TT')
print(str_e)

a = str_a.find('ing')
print(a)
print(' type is', type(a))

a = str_a.find('x')
print(a)
print(' type is', type(a))

str_f = str_b.strip()
print(str_f)

a = str_a.split()
print(a)
print(' type is',type(a))
