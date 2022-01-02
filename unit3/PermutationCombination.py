
a=['a','b','c','d', 'e']

def permute(done_permute, current_permute, remain_item):
    if not remain_item:
        done_permute.append(current_permute)
    else:
        for item in remain_item:
            next_permute = current_permute.copy()
            next_permute += [item]
            new_remain_item = remain_item.copy()
            new_remain_item.remove(item)
            permute(done_permute,next_permute,new_remain_item)

def choose_any(choosen, current_list, remain, i):
    if i == 0:
        choosen.append(current_list)
    else:
        for item in remain:
            next_list = current_list.copy()
            next_list += [item]
            new_remain = remain.copy()
            new_remain.remove(item)
            choose_any(choosen, next_list, new_remain, i-1)
        
def comb_any(choosen, current_list, remain, i):
    if i==0:
        choosen.append(current_list)
    else:
        while remain:
            item = remain.pop(0)
            next_list = current_list.copy()
            next_list += [item]
            new_remain = remain.copy()
            choose_any(choosen, next_list, new_remain, i-1)


choosen=[]
choose_any(choosen,[],a,2)
print(choosen)
print(a)

