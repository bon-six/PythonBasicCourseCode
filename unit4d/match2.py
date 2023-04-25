
greeting = ('Alice','Bob')

match greeting:
    case "":
        print("Hello!")
    case []:
        print("Hello, Empty!")
    case [*names]:
        for name in names:
            print(f"Hi {name}!")
        print("Hi to you all!")
    case name:
        print(f"Hi {name}!")

