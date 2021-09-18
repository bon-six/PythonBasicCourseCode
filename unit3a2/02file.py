import pathlib

file_path = pathlib.Path('./test.txt')
file = file_path.open('w')

# file = open('./test.txt','w')

file.write('this is fist line writen into the file\n')
file.write('and here the second line.\n and third line together.\n')

file.close()
