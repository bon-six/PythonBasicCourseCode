

def foo():
    print('say foo...')
    return

def my_decorator(func):
    def wrapper():
        # do something before
        print('before doing foo...')
        func()
        print('after done foo...')

    return wrapper

# call foo() before apply the decorator
foo()

# apply decorator then call foo again
foo = my_decorator(foo)
foo()

import functools
import math

def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before doing the func call...')
        result = func(*args, **kwargs)
        print('after done the func call...')
        return result
    return wrapper

@my_decorator2
def circle_area(r):
    print(f'inside the func call, parameter is {r}')
    return math.pi*r*r

print(circle_area.__name__)
#circle_area = my_decorator2(circle_area)
print(circle_area(5))
