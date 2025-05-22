from karel.stanfordkarel import *

def main():
    while front_is_clear():
        repair_column()
        move_to_next_column()
    repair_column()  # To fix the last column

def repair_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def move_to_next_column():
    for _ in range(4):
        move()

def turn_around():
    turn_left()
    turn_left()
if __name__ == '__main__':
    main()
