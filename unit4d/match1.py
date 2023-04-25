
class Foo():
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 0
    pass

the_day = Foo.MON
the_day = 'Sunday'
the_day = Foo.SUN

match the_day:
    case Foo.MON | Foo.TUE | Foo.WED | Foo.THU | Foo.FRI:
        print('work day')

    case Foo.SAT:
        print('rest')

    case Foo.SUN:
        print('rest a')

    case _:
        print("don't know")
