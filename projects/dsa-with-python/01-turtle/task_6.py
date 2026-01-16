import turtle

n = 12
full_circle_degrees = 360
angle = full_circle_degrees / n

while n != 0:
    turtle.right(angle)
    turtle.forward(50)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
    n -= 1

distance = 10
while True:
    turtle.forward(distance)
    turtle.left(90)
    distance += 10