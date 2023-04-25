

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

words_counts = {}

while words_list:
    # count each word how many times appeared
    w = words_list[0]
    n = words_list.count(w)
    words_counts[w] = n
    for i in range(0,n):
        words_list.remove(w)

for (word, counts) in words_counts.items():
    print(word, ':', counts)
