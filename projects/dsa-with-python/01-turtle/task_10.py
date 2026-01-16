import turtle
import math

radius = 20

def draw_circle(radius = 60, direction = "left"):
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

def draw_flower(leaves_count):
    for _ in range(leaves_count // 2):
        draw_circle()
        draw_circle(direction="right")
        turtle.left(360 // leaves_count)

    
draw_flower(6)