
def checkOddEven(n):
    if n == 0:
        return 'even'
    elif n == 1:
        return 'odd'
    else:
        return checkOddEven(n-2)
n=19
print(f'number {n} is', checkOddEven(n))


def checkPuzzle(n, history):
    if n*3 == target:
        return '('+history+')*3'
    elif n+5 == target:
        return '('+history+')+5'
    elif n>target:
        return ''
    else:
        result = checkPuzzle(n*3, '('+history+')*3')
        if result == '':
            result = checkPuzzle(n+5, '('+history+')+5')
        return result

target = input("give a number\n")

target = int(target)

result = checkPuzzle(1,'1')
if result == '':
    print('Cannot make this number')
else:
    print(result)



