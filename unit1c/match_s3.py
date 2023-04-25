
score = 98

match score:
    case x if x>85:
        print('excellent')
        print(f'{x:10d}')
    case x if x>70:
        print('good')
        print(f'{x:10d}')
    case x if x>60:
        print('normal')
        print(f'{x:10d}')
    case x if x>=0:
        print('Need Improve')
        print(f'{x:10d}')
    case _:
        print('Unknown score')
