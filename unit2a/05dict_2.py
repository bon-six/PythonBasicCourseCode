
dict_2 = {}

print(dict_2)

if not dict_2:
    print('Empty dict')

dict_2['Sam'] = 'football'
if dict_2:
    print('dict_2 has something, not empty')
    print(dict_2)

dict_2.clear()
print()

dict_2['Sam'] = 'football'
print(dict_2)

dict_2['Tom'] = 'swimming'
print(dict_2)

dict_2['Sam'] = 'badminton'
print(dict_2)

dict_2['Sam'] = ['football','badminton']
print(dict_2)

dict_2['Jason'] = 'basketball'
print(dict_2)
dict_2.pop('Tom')
print(dict_2)
