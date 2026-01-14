#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    has_reached_left = False
    has_reached_right = False

    while True:
        if wall_is_above():
            if wall_is_on_the_left():
                has_reached_left = True
            elif wall_is_on_the_right():
                has_reached_right = True

            if not has_reached_left:
                move_left()
            elif not has_reached_right:
                move_right()
            else:
                break

        else:
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
