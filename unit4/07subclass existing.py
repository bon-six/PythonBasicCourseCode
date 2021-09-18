
class MyList (list):
    pass


mylist_1 = MyList()

mylist_1.append('the first')

mylist_1.append('and second')

mylist_1.append('then third')

print(mylist_1)
print(type(mylist_1))
print()

mylist_1.sort()
print(mylist_1)
print(type(mylist_1))
print()



class MyAnotherList (list):
    # override with new sort mechanism.
    def sort(self):
        print('new sort',self)
        store = None
        for i in range(len(self)):
            if self[i].find('first')>0:
                store = self[i]
                break
            else:
                continue
        temp = self[0]
        self[0] = store
        store = temp
        store = None
        for i in range(1,len(self)):
            if self[i].find('second')>0:
                store = self[i]
                break
            else:
                continue
        temp = self[1]
        self[1] = store
        store = temp
        print(self)
        

mylist_2 = MyAnotherList()

mylist_2.append('then third')

mylist_2.append('the first')

mylist_2.append('and second')

print(mylist_2)
print(type(mylist_2))
print()

mylist_2.sort()
print(mylist_2)
print(type(mylist_2))
print()
