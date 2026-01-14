#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled_count = 0

    while True:
        
        if cell_is_filled():
            filled_count += 1

        if filled_count == 5:
            return
        
        move_right()


if __name__ == '__main__':
    run_tasks()
