
import turtle

s = turtle.Screen()
s.title('My Turtle Drawing')
s.bgcolor('white')
t = turtle.Pen()
t.shape('classic')
t.shapesize(1,1,1)
t.pen(pencolor='red', fillcolor='green', pensize=3, speed=5)

t.begin_fill()

for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()

t.goto(100,100)
t.pendown()
t.circle(60)

t.end_fill()

turtle.done()
#s.mainloop()


#'''
#Name                       Red  Green  Blue
#antique white              250   235   215
#aquamarine                 127   255   212
#azure                      240   255   255
#black                        0     0     0
#blue                         0     0   255
#blue violet                138    43   226
#brown                      165    42    42
#chocolate                  210   105    30
#coral                      255   127    80
#cyan                         0   255   255
#dark blue                    0     0   139
#dark cyan                    0   139   139
#dark green                   0   100     0
#dark grey                  169   169   169
#dark magenta               139     0   139
#dark orange                255   140     0
#dark red                   139     0     0
#dark salmon                233   150   122
#dark violet                148     0   211
#deep pink                  255    20   147
#deep sky blue                0   191   255
#dim grey                   105   105   105
#firebrick                  178    34    34
#floral white               255   250   240
#forest green                34   139    34
#ghost white                248   248   255
#gold                       255   215     0
#green                        0   255     0
#green yellow               173   255    47
#grey                       190   190   190
#honeydew                   240   255   240
#hot pink                   255   105   180
#indian red                 205    92    92
#ivory                      255   255   240
#khaki                      240   230   140
#lavender                   230   230   250
#lawn green                 124   252     0
#light blue                 173   216   230
#light coral                240   128   128
#light cyan                 224   255   255
#light goldenrod            238   221   130
#light green                144   238   144
#light grey                 211   211   211
#light pink                 255   182   193
#light salmon               255   160   122
#light yellow               255   255   224
#lime green                  50   205    50
#linen                      250   240   230
#magenta                    255     0   255
#medium blue                  0     0   205
#medium orchid              186    85   211
#medium purple              147   112   219
#midnight blue               25    25   112
#misty rose                 255   228   225
#moccasin                   255   228   181
#navy blue                    0     0   128
#orange                     255   165     0
#orange red                 255    69     0
#orchid                     218   112   214
#pink                       255   192   203
#plum                       221   160   221
#purple                     160    32   240
#red                        255     0     0
#rosy brown                 188   143   143
#royal blue                  65   105   225
#saddle brown               139    69    19
#salmon                     250   128   114
#sandy brown                244   164    96
#sea green                   46   139    87
#sky blue                   135   206   235
#snow                       255   250   250
#spring green                 0   255   127
#tomato                     255    99    71 
#turquoise                   64   224   208
#violet                     238   130   238
#wheat                      245   222   179
#white                      255   255   255
#yellow                     255   255     0
#yellow green               154   205    50
#'''
