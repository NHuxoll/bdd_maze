import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):

        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entry_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_right_wall,
            False,
        )

        def test_maze_cell_reset_after_init(self):
            num_cols = 12
            num_rows = 10
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=0)
            for j in range(len(m1._cells) - 1):
                for i in range(len(m1._cells[j]) - 1):

                    self.assertEqual(
                        m1._cells[i][j]._visited,
                        False,
                    )


if __name__ == "__main__":
    unittest.main()
