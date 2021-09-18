
word = input('give me a word\n>>>')

save_copy = word

while word:
    if word[0] == word[-1]:
        if len(word) == 1 or len(word) == 2:
            print(f'Yes, {save_copy} is Palindrome word!')
            word = ''
        else:
            word = word[1:-1]
    else:
        print(f'No, {save_copy} is not Palindrome word.')
        word = ''
