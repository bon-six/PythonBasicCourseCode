

value ='abc'
value = 5
value = 0.2
value = int(3.1)
value = True
value = False
value = (1,)
value = [1,2]

match value:
    case str(message):
        print(f'string message is {message}')
    case float(number):
        print(f'float is {number}')
    case bool(judge):
        print(f'bool judgement is {judge}')
    case int(number):
        print(f'integer is {number}')
    case tuple(collect_tuple):
        print(f'tuple is {collect_tuple}')
    case list(collect_list):
        print(f'list is {collect_list}')
    case _:
        print('others')
