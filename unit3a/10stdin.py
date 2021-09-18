
# method 1: use input()
"""
answer = input('What is your name?>>>\n')
print('Hello', answer)
"""

# method 2: use sys.stdin
'''
import sys

for line in sys.stdin:
    print('ECHO..', line, end='')
'''

# method 3: use fileinput

import fileinput

for line in fileinput.input():
    print('Echo  ', line, end='')
    print('filename is ', fileinput.filename())

fileinput.close()
