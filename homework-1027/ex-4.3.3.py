import turtle


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


bob = turtle.Turtle()
polygon(bob, 250, 5)

turtle.mainloop()
