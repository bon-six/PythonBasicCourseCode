
collection = (1,())
collection = (1,(2,))
collection = (1,(2,3,4))
collection = (1,2)
collection = (1,2,3,4)
collection = (1,(2,3),4)

match collection:
    case 1, [x, *others]:
        print("Got 1 and a nested sequence")
        print(f"   in nested: {x} and {others}")
    case (1, x):
        print(f"Got 1 and {x}")
    case it_self:
        print(f"{it_self}")

