
dict1 = {}

dict1['name'] = 'Sam'
dict1['age'] = 12
dict1['food'] = 'ice cream'
dict1['sport'] = 'football'

keys = list(dict1.keys())
keys.append('place')

values = list(dict1.values())
values.append('legoland')
values.append('disneyland')

dict2 = dict(zip(keys,values))

print(list(dict2.items()))
