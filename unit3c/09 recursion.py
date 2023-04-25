
'''
def chicken():
    print('I must be hatched from an egg.')
    egg()
    return

def egg():
    print('I must be laid by a chicken')
    chicken()
    return


print("a chicken trying to find it's ancestor")
chicken()
'''



def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


print(power(4,2))



def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
