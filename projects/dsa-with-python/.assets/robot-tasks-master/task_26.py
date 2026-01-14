#!/usr/bin/python3

from pyrob.api import *

def draw_cross():
    move_right()
    fill_cell()

    for _ in range(2):
        move_down()
        fill_cell()

    move_left()
    move_up()
    fill_cell()
    move_right(2)
    fill_cell()


@task(delay=0.02)
def task_2_4():
    for y in range(5):
        for x in range(10):
            draw_cross()

            if x != 9:
                move_right(2)
                move_up()
            else:
                break

        if y != 4:
            move_down(3)
        else:
            move_up(1)

        move_left(38)

if __name__ == '__main__':
    run_tasks()
