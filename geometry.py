from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self._p1: Point = p1
        self._p2: Point = p2

    def draw(self, canvas: Canvas, fill_colour: str = "black"):
        canvas.create_line(
            self._p1.x,
            self._p1.y,
            self._p2.x,
            self._p2.y,
            fill=fill_colour,
            width=2,
        )


class Cell:
    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1: int | None = None
        self._x2: int | None = None
        self._y1: int | None = None
        self._y2: int | None = None
        self._win = win
        self.exists: bool = True
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win:
            if self.has_left_wall:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, "white")
            if self.has_top_wall:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line)
            else:

                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, "white")
            if self.has_right_wall:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line)
            else:

                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, "white")
            if self.has_bottom_wall:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line)
            else:

                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo: bool = False):
        colour = "gray" if undo else "red"
        center2_x = abs(to_cell._x2 + to_cell._x1) // 2
        center2_y = abs(to_cell._y2 + to_cell._y1) // 2
        if self._x1 and self._x2 and self._y1 and self._y2 and self._win:
            center_x = abs(self._x2 + self._x1) // 2
            center_y = abs(self._y2 + self._y1) // 2
            line = Line(Point(center_x, center_y), Point(center2_x, center2_y))
            self._win.draw_line(line, colour)
