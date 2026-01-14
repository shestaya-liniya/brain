#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    margin = 0
    move_right()
    
    while True:
        for _ in range(margin):
            if wall_is_on_the_right():
                return
            move_right()

        fill_cell()

        margin +=1 

if __name__ == '__main__':
    run_tasks()
