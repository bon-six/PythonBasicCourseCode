
mark = 2

match mark:
    case 9:
        rate = 'Very High'
    case 8:
        rate = 'High'
    case 7:
        rate = 'Above Average'
    case 4|5|6:
        rate = 'Average'
    case 3:
        rate = 'Below Average'
    case 1|2:
        rate = 'Low'
    case _:
        rate = 'Wrong Mark Value'

print(rate)
