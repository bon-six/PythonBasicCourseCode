
a_list = ['one', 'two', 'three', 'four']


i=0
for item in a_list:
    print (item)
    la = len(a_list)
    i +=1
    print(i)
    print(la)
    del a_list[0]
    input()

print(a_list)
