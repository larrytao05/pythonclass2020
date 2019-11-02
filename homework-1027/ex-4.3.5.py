import turtle


def arc(t, r, angle,):

    c = 22 / 7 * r * 2
    for i in range(angle):
        t.fd(c / 360)
        t.lt(1)


bob = turtle.Turtle()
arc(bob, 150, 180)

turtle.mainloop()
