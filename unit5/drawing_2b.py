

import turtle


t = turtle.Pen()
s = turtle.Screen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.speed(0)

# spinral circles, 4

for i in range(100):
    t.circle(i)
    t.left(92)


turtle.done()







