import time
from geometry import Cell, Line, Point
from window import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win=None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = [
            ([Cell(self._win)] * self._num_rows) for i in range(self._num_cols)
        ]
        for i, cols in enumerate(self._cells):
            for j, cell in enumerate(cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw(
            self.cell_size_x * i + self._x1,
            self.cell_size_y * j + self._y1,
            self.cell_size_x * (i + 1) + self._x1,
            self.cell_size_y * (j + 1) + self._y1,
        )
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)
