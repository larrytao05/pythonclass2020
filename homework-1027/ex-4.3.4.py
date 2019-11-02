import turtle


def circle(t, r):
    c = 22 / 7 * r * 2
    for i in range(360):
        t.fd(c / 360)
        t.lt(1)


bob = turtle.Turtle()
circle(bob, 150)

turtle.mainloop()
