
MAX_INT = 100

value = (400,50)
value = (400, 400)
value = (50, 50)
value = (50,20)
value = 300
value = 50
value = None
value = (30,40,50)

match value:
    case [x, y] if x > MAX_INT and y > MAX_INT:
        print("Got a pair of large numbers")
    case [x, y] if x == y:
        print("Got equal items")
    case [x, y]:
        print("Got a pair. not equal, not large")
    case x if x > MAX_INT:
        print("Got a large number")
    case _:
        print("Not an outstanding input")
