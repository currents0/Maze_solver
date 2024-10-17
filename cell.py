from window import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.win == None:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"
        c1 = Point(((self.x2 - self.x1)//2) + self.x1, ((self.y2 - self.y1)//2) + self.y1)
        c2 = Point(((to_cell.x2 - to_cell.x1)//2) + to_cell.x1, ((to_cell.y2 - to_cell.y1)//2) + to_cell.y1)
        line = Line(c1, c2)
        self.win.draw_line(line, color)