
l1 = [1,2,3,[4,5,6]]

def replace_item(collections):
    for item in collections:
        print (item)
    collections[0] = 3
    collections[3][0] = 10
    print(collections)

print(l1)

replace_item(l1)

print(l1)
