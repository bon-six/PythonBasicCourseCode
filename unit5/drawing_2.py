

import turtle


t = turtle.Pen()
s = turtle.Screen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.pencolor('black')
t.pensize(1)
t.speed(1)


# spinral square


for i in range(50):
    t.forward(3*i)
    t.right(90)


turtle.done()







