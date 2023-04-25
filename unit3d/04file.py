
import pathlib

with (path:=pathlib.Path('./article1.txt')).open('r') as file:
    print(''.join(file.readlines()))

print (path)
print(pathlib.Path.cwd()/path)
'''
with open('article1.txt','r') as file:
    print(file.readlines())

with open('test.txt','w') as file:
    file.write('first line\n')

with open('test.txt','a') as file:
    file.write('second line appended\n')
'''
