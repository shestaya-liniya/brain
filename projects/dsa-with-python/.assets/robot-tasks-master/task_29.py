#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    filled_count = 0

    while True:
        
        if cell_is_filled():
            filled_count += 1

        if not cell_is_filled():
            filled_count = 0

        if filled_count == 3:
            return
        
        if not wall_is_on_the_right():
            move_right()
        else:
            return


if __name__ == '__main__':
    run_tasks()
