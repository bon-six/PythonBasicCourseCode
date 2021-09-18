
VOWELS = 'AEIOU'

word = input('Give me a secret word string')

while not word.isalpha():
    print('Give word string only alphabetic letters',end='')
    word = input()

word=word.upper()
kevin_score = 0
stuart_score = 0
pos=0
for c in word:
    if c in VOWELS:
        kevin_score += len(word)-pos
    else:
        stuart_score += len(word)-pos
    pos+=1

if kevin_score == stuart_score:
    print('game draw!')
elif kevin_score > stuart_score:
    print('Kevin Win! Score', kevin_score)
else:
    print('Stuart Win! Score', stuart_score)
