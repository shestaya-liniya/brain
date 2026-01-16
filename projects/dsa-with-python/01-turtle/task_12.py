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


turtle.left(90)

for _ in range(10):
    draw_semi_circle()
    draw_semi_circle(10)