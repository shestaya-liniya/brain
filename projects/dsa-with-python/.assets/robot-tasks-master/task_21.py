#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()

    x = 0
    for y in range(13):
        fill_cell()
        for _ in range(x):
            move_right()
            fill_cell()
        for _ in range(x):
            move_left()
        move_down()
        x += 1




if __name__ == '__main__':
    run_tasks()
