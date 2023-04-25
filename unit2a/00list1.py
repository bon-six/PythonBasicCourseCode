list_1=[0,0,0,0]
print(list_1)
print()

list_1=[]
for i in range(4):
    list_1.append(0)
print(list_1)
print()

list_2=[0 for i in range(4)]
print(list_2)
print()

list_3 = [0]*4
print(list_3)
print()

list_4 = [[0 for i in range(4)] for j in range (3)]
print(list_4)
list_4[0][0]='A'
print(list_4)
print()

list_5 = [[0]*4]*3
print(list_5)
list_5[0][0]='A'
print(list_5)
print()


