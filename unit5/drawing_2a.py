

import turtle


t = turtle.Pen()
s = turtle.Screen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.speed(5)


# spinral circle


for i in range(60):
    t.circle(i*2,60)

turtle.done()







