def find_maximum(items):
    if not items:
        return None
    maximum = items[0]
    for item in items:
        if item > maximum:
            maximum = item
    return maximum

print(find_maximum([]))


list1 = [(10,11,20,7),(5,),(1,3,2),(2,),(3,4)]

def v_item(item):
    return item[-1]

list1.sort(key=v_item)
print(list1)


students = { 'id1': {'name':'Carl','class':'I','subjects':['math','eng','science']},
             'id2': {'name':'Tom','class':'III','subjects':['eng','chn','math']},
             'id3': {'name':'Sophie','class':'IV','subjects':['eng','chn','math']},
             'id4': {'name':'Tom','class':'III','subjects':['eng','chn','math']},
             }
result={}
for student_id, student_info in students.items():
    if student_info not in result.values():
        result[student_id] = student_info

print(result)



letters = {1:['a','b'], 2:['d','e','f']}
combinations = []
for letter1 in letters[1]:
    for letter2 in letters[2]:
        combinations.append(letter1+letter2)
print(combinations)


str_a = 'abcdc'
counter = {}
for c in str_a:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1
print(counter)



my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
