
text1 = input('Please give me a string.\n')

VOWELS = 'aeiou'

for vowel in VOWELS:
    counts = text1.count(vowel)
    counts += text1.count(vowel.upper())
    print(vowel, ':', counts)



def count_char(text, char):
    if not text:
        return 0
    count = 0
    for a in text:
        if a == char:
            count += 1
    return count



