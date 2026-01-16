import turtle
import math

def find_rectangle_side_len(sides_count, radius):
    return 2 * radius * math.sin(math.pi/sides_count)

def draw_regular_rectangle(sides_count, radius):
    angle = 360 / sides_count

    side_len = find_rectangle_side_len(sides_count, radius)
    
    for x in range(sides_count):
        if x == 0:
            turtle.left(angle / 2)
        else:
            turtle.left(angle)

        turtle.forward(side_len)

    turtle.left(angle)
    turtle.right(angle / 2)

radius = 10

for angles in range(3, 14):
    draw_regular_rectangle(angles, radius)
    radius += 10

    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()

turtle.done()