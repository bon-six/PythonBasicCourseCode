

def reverseWithNew(li):
    new_li = []
    for x in li:
        new_li.insert(0,x)
    return new_li


def reverseInPlace(li):
    for x in range(len(li)//2):
        li[x], li[-x-1] = li[-x-1], li[x]

l1 = []
# l1 = [i for i in range(101)]

print('Original')
print(l1)

l2=reverseWithNew(l1)
print('Reversed')
print(l2)


reverseInPlace(l1)
print('Reversed')
print(l1)

