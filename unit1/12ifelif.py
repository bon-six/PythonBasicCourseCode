

score = input('give me a score(1~5)>>> ')
score = int(score)

if score==5:
    print('excellent')
elif score == 4:
    print('very good')
elif score ==3:
    print('good')
elif score==2:
    print('need improve')
else:
    print('need great improve')
