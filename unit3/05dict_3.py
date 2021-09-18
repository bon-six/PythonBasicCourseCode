
dict_1 = {'Sam':'football',
          'Tom':'swimming',
          'Jason':'basketball',
          'Alice':'dance'}
print(dict_1)
print()


dict_1 = {}
dict_1['Sam']='football'
dict_1['Tom']='swimming'
dict_1['Jason']='basketball'
dict_1['Alice']='dance'
print(dict_1)
print()

list_1=['Sam','Tom','Jason','Alice']
dict_1=dict.fromkeys(list_1,'Unknown')
#when the value is an mutable object in above code, careful of shallow copy
print(dict_1)
print()

list_2=['football','swimming','basketball','dance']
dict_1=dict(zip(list_1,list_2))
print(dict_1)
print()
