import turtle
import math

def find_rectangle_side_len(sides_count, radius):
     return 2 * radius * math.sin(math.pi/sides_count)

def draw_star(angles_count, radius):
    polygon_angle = 360 / angles_count
    side_len = find_rectangle_side_len(angles_count, radius)

    for _ in range(angles_count):
        turtle.forward(side_len)
        turtle.left(polygon_angle * (angles_count // 2 + 1 ))

# draw_star(5, 50)
draw_star(20, 200)


turtle.done()