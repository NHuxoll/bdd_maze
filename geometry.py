
from tkinter import Canvas

import window


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

class Cell:
    def __init__(self, x1: int, x2: int, y1:int, y2:int, has_left_wall: bool = True, has_right_wall: bool = True, has_top_wall: bool= True, has_bottom_wall: bool=True ) -> None:
        self.has_left_wall: bool = has_left_wall
        self.has_right_wall: bool = has_right_wall
        self.has_top_wall: bool  = has_top_wall
        self.has_bottom_wall: bool  = has_bottom_wall
        self.___x1: int = x1 
        self.___x2: int = x2 
        self.___y1: int = y1 
        self.___y2: int = y2 
        self.___win: window.Window
        self.exists:bool = True

    def draw(self):
        pass
