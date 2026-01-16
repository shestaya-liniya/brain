#!/usr/bin/python3
import math

from pyrob.api import *

def calc_square_side_len():
    x = 1
    while not wall_is_on_the_right():
        move_right()
        x += 1

    move_left(x - 1)
    return x



@task(delay=0)
def task_9_3():
    square_len = calc_square_side_len()
    initial_triangle_len = square_len - 2

    for _ in range(math.floor(square_len / 2)):

        for _ in range(initial_triangle_len):
            move_right()
            fill_cell()

        move_right()

        for _ in range(initial_triangle_len):
            move_down()
            fill_cell()

        move_down()

        for _ in range(initial_triangle_len):
            move_left()
            fill_cell()

        move_left()

        for _ in range(initial_triangle_len):
            move_up()
            fill_cell()

        move_up()
        
        move_down()
        move_right()

        initial_triangle_len -= 2

    move_down(square_len // 2)
    move_left(square_len // 2)

if __name__ == '__main__':
    run_tasks()
