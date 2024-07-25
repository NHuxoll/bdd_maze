from window import Window
from geometry import Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 15, 20, 40, 40, win, 1337)
    win.wait_for_close()


main()
