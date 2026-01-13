import turtle
import math

# Draw circle
# x = 0
# while x < 36:
#     turtle.forward(10)
#     turtle.left(10)
#     x += 1

# turtle.done()

# Draw 10 nested squares
# square_side_len = 20
# x = 0
# while x < 10:
#     y = 0
#     while y < 4:
#         turtle.forward(square_side_len)
#         turtle.left(90)
#         y += 1
#     turtle.right(90)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.right(90)
#     turtle.forward(10)
#     turtle.right(180)
#     turtle.pendown()
#     square_side_len += 20
#     x += 1

# Draw a spider network for N stripes
# n = 12
# full_circle_degrees = 360
# angle = full_circle_degrees / n

# while n != 0:
#     turtle.right(angle)
#     turtle.forward(50)
#     turtle.stamp()
#     turtle.right(180)
#     turtle.forward(50)
#     turtle.right(180)
#     n -= 1

# distance = 10
# while True:
#     turtle.forward(distance)
#     turtle.left(90)
#     distance += 10

# draw nested regular polygons

circle_angle = 360
initial_radius = 50

def find_regular_polygon_inner_angle(angles):
    return 180*(angles - 2)/angles

def draw_regular_polygon(angles, radius):
    current_angle = circle_angle / angles
    k = 0
    while k < angles:
        turtle.left(current_angle)
        turtle.forward(find_rectangle_side_len(angles, radius))
        k += 1

def find_rectangle_side_len(angles, radius):
    return 2 * radius * math.sin(math.radians(180 / angles))

for x in range(3,5,1):
    draw_regular_polygon(x, initial_radius)
    initial_radius += 20
    turtle.forward(10)
    # turtle.penup()
    # turtle.forward(20)
    # turtle.pendown()
    # turtle.left(circle_angle / x)
    # turtle.forward(find_rectangle_side_len(x, initial_radius))

turtle.done()

