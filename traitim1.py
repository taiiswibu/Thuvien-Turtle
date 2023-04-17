import turtle

t = turtle.Turtle()

t.speed(0)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.begin_fill()
t.color('#FF69B4') # Set màu hồng cho trái tim
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()

turtle.done()
