#!/usr/bin/python3

from pyrob.api import *

def draw_cross():
    y = 0

    for _ in range(3):
        if y % 2 == 0:
            move_right(1)
            fill_cell()
            move_left()
            move_down()
        else:
            fill_cell()
            for _ in range(2):               
                move_right()
                fill_cell()
            move_left(2)
            move_down()
        y += 1

    move_up(3)
        

        
    

@task
def task_2_1():
    move_right()
    move_down()

    draw_cross()


if __name__ == '__main__':
    run_tasks()
