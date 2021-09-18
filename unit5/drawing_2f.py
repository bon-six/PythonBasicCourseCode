

import turtle


t = turtle.Pen()
s = t.getscreen()

s.title('My Turtle Drawing')
s.bgcolor('white')

t.shape('classic')
t.shapesize(1,1,1)

t.speed(10)
t.pensize(1)

# color solid petal, 6

for i in range(6):
    
    t.setposition(0,0)
    t.pencolor('purple')
    for j in range(50):
        t.forward(1)
        t.dot(j/2)
        
    t.left(60)
    

turtle.done()







