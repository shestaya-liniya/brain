#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    already_filled = 0

    while True:
        if cell_is_filled():
            already_filled += 1

        if (
            not wall_is_above() and
            not wall_is_beneath() and
            not wall_is_on_the_left()
        ):
            break
        
        
        elif (
            not wall_is_beneath() or 
            not wall_is_on_the_right() and wall_is_above()
            ):
            fill_cell()
    
        if not wall_is_above():
            move_up()
            continue
        else:
            while not wall_is_beneath():
                move_down()

        move_right()
    
    mov('ax', already_filled)


if __name__ == '__main__':
    run_tasks()
