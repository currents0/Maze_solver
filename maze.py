from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if j > 0 and not self.cells[i][j-1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self.cells[i][j+1].visited:
                to_visit.append((i, j + 1))
            if i > 0 and not self.cells[i-1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self.cells[i+1][j].visited:
                to_visit.append((i + 1, j))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            visit_next = random.randrange(len(to_visit))
            if to_visit[visit_next][1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
            if to_visit[visit_next][1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
            if to_visit[visit_next][0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
            if to_visit[visit_next][0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
            self._break_walls_r(to_visit[visit_next][0], to_visit[visit_next][1])

    def _reset_cells_visited(self):
        for column in self.cells:
            for cell in column:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        if j > 0 and not self.cells[i][j-1].visited and not self.cells[i][j-1].has_bottom_wall:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            solved = self._solve_r(i, j-1)
            if solved:
                return True
            self.cells[i][j].draw_move(self.cells[i][j-1], True)
        if j < self.num_rows - 1 and not self.cells[i][j+1].visited and not self.cells[i][j+1].has_top_wall:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            solved = self._solve_r(i, j+1)
            if solved:
                return True
            self.cells[i][j].draw_move(self.cells[i][j+1], True)
        if i > 0 and not self.cells[i-1][j].visited and not self.cells[i-1][j].has_right_wall:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            solved = self._solve_r(i-1, j)
            if solved:
                return True
            self.cells[i][j].draw_move(self.cells[i-1][j], True)
        if i < self.num_cols - 1 and not self.cells[i+1][j].visited and not self.cells[i+1][j].has_left_wall:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            solved = self._solve_r(i+1, j)
            if solved:
                return True
            self.cells[i][j].draw_move(self.cells[i+1][j], True)
        return False