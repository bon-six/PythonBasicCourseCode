
VOWELS = 'AEIOU'

word = input('Give me a secret word string')

while not word.isalpha():
    print('Give word string only alphabetic letters',end='')
    word = input()

word=word.upper()
kevin_score = 0
stuart_score = 0

for i in range(len(word)):
    for j in range(i,len(word)):
        sub_string = word[i:j+1]
        for vowel in VOWELS:
            if sub_string.startswith(vowel):
                kevin_score+=1
                break
        else:
            stuart_score+=1


if kevin_score == stuart_score:
    print('game draw!')
elif kevin_score > stuart_score:
    print('Kevin Win! Score', kevin_score)
else:
    print('Stuart Win! Score', stuart_score)
