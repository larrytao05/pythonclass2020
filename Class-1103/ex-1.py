# turtle race
import turtle
import random


def race(t, n, f):
    t.penup()
    n.penup()
    f.penup()
    t.lt(90)
    n.fd(100)
    n.lt(90)
    f.lt(180)
    f.fd(100)
    f.rt(90)
    t.pendown()
    n.pendown()
    f.pendown()

    for i in range(10):
        t.fd(random.randrange(1, 50, 1))
        n.fd(random.randrange(1, 50, 1))
        f.fd(random.randrange(1, 50, 1))


bob = turtle.Turtle()
larry = turtle.Turtle()
maggot = turtle.Turtle()
race(bob, larry, maggot)

turtle.mainloop()