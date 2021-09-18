
for i in range(1,101):
    if i%2 == 0:
        print(i, ' is even')
    else:
        print(i, ' is odd')


score = input('please give score (1~5)\n')
score = int(score)
if score == 5:
    print('Execellent, Outstanding')
elif score == 4:
    print('Great, High')
elif score == 3:
    print('Good, Sound OK')
elif score == 2:
    print('Basic')
elif score == 1:
    print('Limited')
else:
    print('Wrong score')


for i in range(1,51):
    if i%3 == 0 and i%7 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%7 == 0:
        print('Buzz')
    else:
        print(i)
    
