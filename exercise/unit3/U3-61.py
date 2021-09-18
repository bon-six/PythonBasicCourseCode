d = {}
d['name'] = 'Sam'
d['age'] = 12
d['food'] = 'cake'
d['sport'] = 'run'
k = list(d.keys())
k.append('color')
v = list(d.values())
v.append('red')
v.append('blue')
d1 = dict(zip(k,v))
print(list(d1.items()))
