import turtle
import math

def draw_semi_circle(radius = 60, direction = "right"):
    p = 2 * math.pi * radius

    steps = 60 # circle detalization

    step_distance = p / steps
    angle = 360 / steps

    print(steps, steps /2, steps//2)

    for _ in range(steps // 2):
        turtle.forward(step_distance)

        if direction == "left":
            turtle.left(angle)
        elif direction == "right":
            turtle.right(angle)

    turtle.forward(step_distance) # how to eliminate?


def draw_circle(radius = 60, direction = "right"):
    p = 2 * math.pi * radius

    steps = 60 # circle detalization

    step_distance = p / steps
    angle = 360 / steps

    for _ in range(steps):
        turtle.forward(step_distance)

        if direction == "left":
            turtle.left(angle)
        else:
            turtle.right(angle)


def draw_colored_circle(radius, color, x = None, y = None):
    
    if x and y:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    turtle.color(color)
    turtle.begin_fill()
    draw_circle(radius)
    turtle.end_fill()

turtle.speed(100)

draw_colored_circle(100, "#ffff00")
draw_colored_circle(10, "#0000ff", -33,-30)
draw_colored_circle(10, "#0000ff", 33,-30)

turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.color("#000")
turtle.width(4)
turtle.right(90)
turtle.forward(20)
# turtle.width(1)

turtle.penup()
turtle.goto(-50, -140)
turtle.pendown()

draw_semi_circle(50, "left")


turtle.done()


