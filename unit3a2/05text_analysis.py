
with open('article2.txt',mode='r') as file:
    article_content = file.read()

to_bereplaced = ',.?!:"-()$@&%0123456789'
# replace any non wording letters with space
for c in to_bereplaced:
    article_content = article_content.replace(c,' ')  

# change all to lowercase, uppercase and lowercase words count as same.
article_content = article_content.lower()

words_list = article_content.split()

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
