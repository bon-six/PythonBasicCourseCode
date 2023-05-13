# importing package
import turtle

s=turtle.Screen()
s.bgcolor('black')

t=turtle.Turtle()
t.pencolor('white')

# loop for motion with
# default tracer as 1
for i in range(20):
    t.forward(1+1*i)
    t.right(45)

# set tracer values as (2,0)
# 2 -> for screen update
# 0 -> delay
s.tracer(n=2, delay=0)
t.pencolor('yellow')
# loop for motion with
# above tracer values
for i in range(20, 40):
    t.forward(1+1*i)
    t.right(45)

# set tracer values as (1,50)
# 1 -> for screen update
# 50 -> delay
s.tracer(n=1, delay=50)
t.pencolor('red')

# loop for motion with
# above tracer values
for i in range(40, 60):
    t.forward(1+1*i)
    t.right(45)

turtle.done()
