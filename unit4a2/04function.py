
import math


def myfactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        n_fac = 1
        for i in range(2, n+1):
            n_fac *= i
        return n_fac

def circle_area(r):
    return math.pi*r*r


f1 = myfactorial

print(f1(3))

print(myfactorial(5))

print(f1 is myfactorial)


def calc(func, arg1):
    return(func(arg1))


print(calc(myfactorial, 4))

print(calc(f1, 3))

print(calc(circle_area, 5))



def give_a_func(i):
    def first_func():
        print('greetings from the first func')
        return

    def second_func():
        print('greetings from the second func')
        return

    if i == 1:
        return first_func
    elif i == 2:
        return second_func
    else:
        return give_a_func

f1 = give_a_func(0)

print(f1 is give_a_func)

f1 = give_a_func(2)
f1()

# direct call will raise error, name is local and glocal cannot see it
# second_func()
