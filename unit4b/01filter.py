


# filter function to take certain part from a list
# the first argument is a function which for each item
# a True or False result for the selection
l1 = [-1, 2, 3.5, -5.4]

result = filter(lambda x: x>0, l1)

# filter result can only be used once.
# if convert it to list, then it becomes empty.
# if use for loop to visit it, then it also becomes empty.
l2 = list(result)
print(l2)

print(result)
for item in result:
    print(item)

l2 = list(result)
print(l2)
