


# map function to make change to each item from a list
# the first argument is a function which for each item
# to make the corresponding changes and give the new mapped item
l1 = ['abc', 'def', 'xyz', 'rst']

result = map(lambda x: x.upper(), l1)


# map result can only be used once.
# if converted to a list, then it becomes empty.
# if use for loop to go through all items, it also becomes empty.
l2 = list(result)
print(l2)

print(result)
for item in result:
    print(item)

l2 = list(result)
print(l2)
