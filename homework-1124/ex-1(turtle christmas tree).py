import turtle
import random


def draw_rectangle(turtle, color, x, y, w, l):

    turtle.speed(5)
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(90)
    turtle.begin_fill()

    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.end_fill()


def draw_star(turtle, color, x, y, l):

    turtle.speed(5)
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-36)
    turtle.begin_fill()

    turtle.forward(l/2)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.end_fill()
    turtle.penup()


def draw_circle(turtle, r, x, y, color):
    turtle.speed(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()

    turtle.circle(r)

    turtle.end_fill()
    turtle.penup()


hi = turtle.Turtle()
turtle.bgcolor("black")
draw_rectangle(hi, "brown", -30, -100, 50, 30)

hi.penup()
hi.goto(-130, -50)
hi.right(90)
hi.pendown()
width = 270
x = -130
y = -50
while width >= 50:
    draw_rectangle(hi, "green", x, y, 30, width - 40)
    width = width - 40
    x = x + 20
    y = y + 30

draw_rectangle(hi, "green", x, y, 10, width - 40)
hi.forward(10)

draw_star(hi, "yellow", x - 10, y + 10, 60)
hi.goto(-375, -80)
hi.color("white")
hi.setheading(0)
hi.pendown()
hi.begin_fill()
hi.forward(345)
hi.right(90)
hi.forward(20)
hi.left(90)
hi.forward(30)
hi.left(90)
hi.forward(20)
hi.right(90)
hi.forward(375)
hi.right(90)
hi.forward(300)
hi.right(90)
hi.forward(750)
hi.right(90)
hi.forward(300)
hi.end_fill()

width = 250
hi.penup()
x = -100
y = -40
z = 5
while width >= 30:
    for i in range(z):
        draw_circle(hi, random.randint(10, 20), random.randint(x, width - 40), random.randint(y, y + 30), "red")
        z -= 1

    x = x + 40
    y = y + 60
    width -= 80





turtle.mainloop()




