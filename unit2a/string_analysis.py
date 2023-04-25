

str_a = input('enter a long string>>>')

# replace any ',' with space
str_a = str_a.replace(',',' ')  

# replace any '.' with space
str_a = str_a.replace('.',' ')  

# if have any other like '?', or '!', also need to replace
str_a = str_a.replace('?',' ')
str_a = str_a.replace('!',' ')

# change all to lowercase, uppercase and lowercase words count as same.
str_a = str_a.lower()

words_list = str_a.split()

words_counts = []

for w in words_list:
    # count each word how many times appeared
    words_counts.append(words_list.count(w))  

# make the word and it's counts associted
result_d = dict(zip(words_list, words_counts))

for (word, counts) in result_d.items():
    print(word, ':', counts)


