list_1 = [1, 3, 5, 7]
print(list_1)
print(' type of list item is', type(list_1[0]))
print()

list_2 = ['dog', 'cat', 'bat', 'tiger', 'wolf']
print(list_2)
print(' type of list item is', type(list_2[0]))
print()

list_3 = ['dog', True, 3, ['walk', 'bite', 'bark']]
print(list_3)
print(' type of list item 0 is', type(list_3[0]))
print(' type of list item 1 is', type(list_3[1]))
print(' type of list item 2 is', type(list_3[2]))
print(' type of list item 3 is', type(list_3[3]))
print()

list_4 = list_3
print(list_4)
list_3[0] = 'cat'
list_3[3][2] = 'meow'
print(list_4)
print()

for item in list_4:
    print(item)
    print(' item type is', type(item))
print('___End!')
