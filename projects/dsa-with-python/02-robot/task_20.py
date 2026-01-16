#!/usr/bin/python3

from pyrob.api import *


@task(delay=0)
def task_4_3():
    move_right()
    for y in range(12):
        for x in range(26):
            fill_cell()
            if y % 2 == 0:
                move_right()
            else:
                move_left()
        fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
