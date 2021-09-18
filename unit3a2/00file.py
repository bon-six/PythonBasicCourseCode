import pathlib

path = pathlib.Path('./article1.txt')

file = path.open('r')

for each_line in file:
    print(each_line)
    input()

file.close()
