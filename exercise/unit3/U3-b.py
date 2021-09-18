

text1 = input('Please give me a sentence.\n')

character_list = []
for c in text1:
    if c == ' ':
        character_list.append('#')
    else:
        character_list.append(c)

new_text = ''.join(character_list)

print(new_text)




text1 = input('Please give me a sentence 1.\n')
text2 = input('Please give me a sentence 2.\n')

common_words = []

words1 = text1.split()
words2 = text2.split()

for word in words1:
    if word in words2:
        common_words.append(word)

print(common_words)


text1 = input('Please give me a sentence.\n')

word_length = 0
word = ''
for w in text1.split():
    if (lw:=len(w)) > word_length:
        word_length = lw
        word = w
print(f"longest word is {word}, it's length is {word_length}")
        
