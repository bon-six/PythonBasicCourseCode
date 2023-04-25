
import copy

list_3 = ['dog', True, 3, ['walk', 'bite','bark']]

print(list_3)
print(' type of list item 0 is', type(list_3[0]))
print(' type of list item 1 is', type(list_3[1]))
print(' type of list item 2 is', type(list_3[2]))
print(' type of list item 3 is', type(list_3[3]))
print()

list_4 = list_3
list_5 = list_3.copy()
list_6 = list(list_3)
list_7 = copy.deepcopy(list_3)

print(list_4)
print(list_5)
print(list_6)
print(list_7)
print()

list_3[0] = 'cat'
list_3[3][2] = 'meow'

print(list_4)
print()

#copy() will potentially have problem for nested mutable
print(list_5)
print()

#list() function is similar like copy()
print(list_6)
print()

print(list_7)
print()

#when extend with list_4, it is same like copy list_4.
#nested mutable will potentially have problem.
list_7.extend(list_4)
print(list_7)
print()
list_4[0]='mouse'
list_4[3][2] = 'squeak'
print(list_7)



