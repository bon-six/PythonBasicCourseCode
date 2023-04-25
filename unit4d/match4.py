

the_value = {'a':1, 'b':[2,20]}
the_value = {'x':100, 'y':200, 'z':300}

match the_value:
    case {'x' : value, **kw_values} | {'y' : value, **kw_values} :
        print(f'from xy, {value}')
        print(f'the rest is {kw_values}')
    case {'a': a_value, **kw_values }:
        print(f'start with a, {a_value}')
        print(f'rest is {kw_values}.')
    case _:
        print('the default')
