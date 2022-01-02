
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    pass

class Rectangle():
    def __init__(self,x0,y0,x1,y1):
        self.point1 = Point(x0,y0)
        self.point2 = Point(x1,y1)
    pass

shape = Rectangle(0,0,200,200)
#shape = Point(2,5)

match shape:
    case Point(x=x0, y=y0):
        print(f'Point located at({x0}, {y0})')
    case Rectangle(point1=Point(x=x0, y=y0), point2=Point(x=x1, y=y1)):
        print(f'Rectangle from Point({x0},{y0}) to Point({x1}, {y1})')
    case _:
        print('Unknown shape')
