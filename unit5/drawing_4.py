
import turtle

t=turtle.Pen()
s = t.getscreen()
# s = turtle.Screen()

s.title('Turtle Drawing')
s.bgcolor('white')

t.color('red', 'yellow')
t.speed(0)

t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

turtle.done()
#s.mainloop()
