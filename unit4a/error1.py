import sys

a = input('give the first number /Numerator >>>')

b = input('give the second number /Denominator >>>')

try:
    a = int(a)
except ValueError:
    print(f'Invalid literal valur for int() base 10: {a}')
else:
    try:
        b = int(b)
    except ValueError as e:
        print(f'Invalid literal value, {e}')
    else:
        try:
            c = a // b
            d = a % b
        except ZeroDivisionError:
            print('Divide by zero: integer division or modulo by zero')
        except:
            print(f'unexpected error happened. {sys.exc_info()[0]}')
        else:
            print(f'{a} = {b} * {c} + {d}')
            
