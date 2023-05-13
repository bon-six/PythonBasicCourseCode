
import turtle

s=turtle.Screen()
t=turtle.Turtle()

t.speed('fastest')
# turning the turtle to face upwards
t.rt(-90)
# the acute angle between
# the base and branch of the Y
angle = 30

# function to plot a Y
def y(sz, level):
    if level > 0:
        s.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        t.pencolor(0, 255//level, 0)

        # drawing the base
        t.fd(sz)
        t.rt(angle)

        # recursive call for
        # the right subtree
        y(0.8 * sz, level-1)

        t.pencolor(0, 255//level, 0)
        t.lt( 2 * angle )

        # recursive call for
        # the left subtree
        y(0.8 * sz, level-1)

        t.pencolor(0, 255//level, 0)
        t.rt(angle)
        t.fd(-sz)

# tree of size 80 and level 7
y(80, 9)
s.mainloop()
