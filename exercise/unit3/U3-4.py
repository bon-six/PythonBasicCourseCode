

a = ['apple','banana','carot','fish']
b = ['rice','bread','cake','fish']
c =[]

for item in a:
    if item in b:
        a.remove(item)
        b.remove(item)
        c.append(item)
    
print(a)
print(b)
print(c)
