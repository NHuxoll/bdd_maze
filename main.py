from window import Window
from geometry import Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 20, 15, 40, 40, win)
    win.wait_for_close()


main()
