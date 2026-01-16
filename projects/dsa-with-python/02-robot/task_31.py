#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    has_reached_left = has_reached_right = False

    while not (
        has_reached_left and
        has_reached_right and
        wall_is_on_the_right()
    ):
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()

            has_reached_left = has_reached_right = False
            continue

        if wall_is_on_the_left():
            has_reached_left = True
        elif wall_is_on_the_right():
            has_reached_right = True

        if not has_reached_left:
            move_left()
        elif not has_reached_right:
            move_right()
        else:
            while not wall_is_on_the_left():
                move_left()
            break



if __name__ == '__main__':
    run_tasks()
