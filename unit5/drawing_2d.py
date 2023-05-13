
import turtle

s = turtle.Screen()
s.title('My Turtle Drawing')
s.bgcolor('white')
t = turtle.Pen()
t.shape('classic')
t.shapesize(1,1,1)
t.speed(0)

# spinral stairs, 3 sides
for i in range(150):
    t.forward(i*2+50)
    t.left(121)

turtle.done()
