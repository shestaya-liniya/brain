import turtle

square_side_len = 20
x = 0
while x < 10:
    y = 0
    while y < 4:
        turtle.forward(square_side_len)
        turtle.left(90)
        y += 1
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    square_side_len += 20
    x += 1


