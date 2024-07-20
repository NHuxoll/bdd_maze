
from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int ) -> None:
        self.x: int =  x 
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.__p1: Point = p1
        self.__p2: Point = p2

    def draw(self, fill_colour: str, canvas: Canvas):
        canvas.create_line(
        self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_colour, width=2
)
