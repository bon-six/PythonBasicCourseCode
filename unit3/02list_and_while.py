

list_3 = ['dog', True, 3, ['walk', 'bite','bark']]

i=0
while i < len(list_3):
    item = list_3[i]
    print (item)
    i+=1
print(list_3)
print()

while list_3:
    item = list_3[0]
    print(item)
    list_3.remove(item)
print (list_3)

print('____End!')
