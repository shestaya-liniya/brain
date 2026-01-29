import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

# consts
support_coords = gr.Point(400, 200)
wire_len = 200
angle = 45

# ball coords
initial_ball_x = wire_len * math.cos(math.radians(45))
initial_ball_y = wire_len * math.sin(math.radians(45))
ball_coords = gr.Point(support_coords.x + initial_ball_x, support_coords.y + initial_ball_y)

# primitives
ball = gr.Circle(ball_coords, 10)
wire = gr.Line(gr.Point(support_coords.x, support_coords.y), gr.Point(ball_coords.x, ball_coords.y))    
support = gr.Line(gr.Point(support_coords.x - 40, support_coords.y),gr.Point(support_coords.x + 40, support_coords.y))

def initial_draw():
    ball.setFill('red')
    ball.draw(window)

    support.setFill("white")
    support.draw(window)

    wire.setFill('white')
    wire.draw(window)


initial_draw()

theta_max = math.radians(45)
omega = math.sqrt(9.81 / wire_len)
t = 0
dt = 0.05

while True:
    t += dt
    theta = theta_max * math.cos(omega * t)

    new_x = support_coords.x + wire_len * math.sin(theta)
    new_y = support_coords.y + wire_len * math.cos(theta)

    dx = new_x - ball.getCenter().x
    dy = new_y - ball.getCenter().y

    ball.move(dx, dy)

    wire.undraw()
    wire = gr.Line(support_coords, gr.Point(new_x, new_y))
    wire.setFill("white")
    wire.draw(window)

    gr.time.sleep(0.02)

window.getMouse()
window.close()
