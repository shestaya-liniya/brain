import turtle
import math

def draw_circle(radius = 60, direction = "left"):
    p = 2 * math.pi * radius

    steps = 60 # circle detalization

    step_distance = p / steps
    angle = 360 / steps

    for _ in range(steps):
        turtle.forward(step_distance)

        if direction == "left":
            turtle.left(angle)
        elif direction == "right":
            turtle.right(angle)

turtle.left(90)

radius = 50

for _ in range(10):
    draw_circle(radius)
    draw_circle(radius, "right")
    radius += 10
    