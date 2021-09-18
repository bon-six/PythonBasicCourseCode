

import turtle


t = turtle.Pen()
s = t.getscreen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.speed(0)


# spinral circles, 3

for i in range(100):
    t.circle(i)
    t.left(121)


turtle.done()







