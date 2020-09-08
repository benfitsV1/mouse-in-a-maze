from tkinter import Tk, Canvas
import random

DIR_RIGHT = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_UP = 3


def get_mazetrix():
    with open("mazetrix.txt") as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines]


def get_mouse_xy():
    for y, row in enumerate(mazetrix):
        x = row.find("M")
        if(x != -1):
            return x, y


def draw_maze():
    for y, row in enumerate(mazetrix):
        for x, ch in enumerate(row):
            if(is_wall(x, y)):
                draw_wall(x, y)


def draw_wall(x, y):
    draw(x, y, "green")

def draw_mouse(x, y):
    draw(x, y, "blue")

def draw_footprint(x, y):
    draw(x, y, "yellow")


def draw(x, y, color):

    maze_height = len(mazetrix)
    maze_width = len(mazetrix[0])
    height = canvas_height/maze_height
    width = canvas_width/maze_width

    x1, y1 = (x*width, y*height)
    x2, y2 = (x1+width, y1+height)
    w.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


def is_wall(x, y):
    return mazetrix[y][x] == '#'

def is_exit(x, y):
    return mazetrix[y][x] == 'E'


random.seed(18)
canvas_height = 450
canvas_width = 750

def main():

    global root, w, mazetrix, x, y
    mazetrix = get_mazetrix()
    x, y = get_mouse_xy()

    root = Tk()
    root.title("Mouse in a Maze")
    w = Canvas(root, bg="white", width=canvas_width, height=canvas_height)
    w.pack()
    draw_maze()
    move_the_mouse()
    root.mainloop()


steps = 0

def move_the_mouse():

    global x, y, steps

    while True:

        new_x, new_y = x, y
        new_direction = get_next_move_random()

        if(new_direction == DIR_RIGHT):
            new_x += 1
        if(new_direction == DIR_DOWN):
            new_y += 1
        if(new_direction == DIR_LEFT):
            new_x -= 1
        if(new_direction == DIR_UP):
            new_y -= 1

        if(not is_wall(new_x, new_y)):
            break

    draw_footprint(x, y)
    x, y = new_x, new_y
    draw_mouse(x, y)

    steps += 1

    if(is_exit(x, y)):
        print("Total steps: " + str(steps))
    else:
        root.after(10, move_the_mouse)



def get_next_move_random():
    dirs = [DIR_RIGHT, DIR_DOWN, DIR_LEFT, DIR_UP]
    return dirs[random.randint(0, len(dirs)-1)]



main()
