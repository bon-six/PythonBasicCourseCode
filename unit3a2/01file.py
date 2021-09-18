
import pathlib

file_path = pathlib.Path('./article1.txt')

file = file_path.open('r')

# file = open('article1.txt','r')

file_content = file.read()
print(file_content)

file.close()

