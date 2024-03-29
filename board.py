import pygame
from typing import List
from cell import Cell

class Board():
    def __init__(self, window:pygame.Surface, font:pygame.font.Font, grid_size:int=600 ):
        self.GRID_LEN = 9
        self.GRID_SIZE = grid_size
        self.CELL_SIZE = grid_size // self.GRID_LEN
        self.CELL_CENTER = self.CELL_SIZE // 3
        self.grid = [[None for _ in range(self.GRID_LEN)] for _ in range(self.GRID_LEN)]
        self.window = window
        self.font = font
        self.rect = pygame.Rect(0, 0, self.GRID_SIZE, self.GRID_SIZE)

    def init_grid(self, board: List[List[str]]):
        self.grid = [[None for _ in range(self.GRID_LEN)] for _ in range(self.GRID_LEN)]
        for x in range(self.GRID_LEN):
            for y in range(self.GRID_LEN):
                cell = Cell(x, y, self.CELL_SIZE, board[x][y], pygame.Rect(x*self.CELL_SIZE, y*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                self.grid[x][y] = cell
        return self.grid
    
    def draw_grid(self):
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid[1])):
                self.grid[x][y].draw_rect(self.window)

    def draw_value(self):
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid[1])):
                self.grid[x][y].draw_value(self.window, self.font)

    def deselect_all(self):
        for row in self.grid:
            for cell in row:
                cell.deselect()

    def find_selected(self):
        for row in self.grid:
            for cell in row:
                if cell.is_selected():
                    return cell.get_position()
        return None
    
    def draw_lines(self, color: tuple=(0,0,255), width: int=3):
        # vertical lines
        for i in range(3, self.GRID_LEN, 3):
            start_pos = (self.CELL_SIZE*i, 0)
            end_pos = (self.CELL_SIZE*i, self.GRID_SIZE)
            pygame.draw.line(surface=self.window, color=color, start_pos=start_pos, end_pos=end_pos, width=width)

        # horizontal lines
        # vertical lines
        for i in range(3, self.GRID_LEN, 3):
            start_pos = (0, self.CELL_SIZE*i)
            end_pos = (self.GRID_SIZE, self.CELL_SIZE*i)
            pygame.draw.line(surface=self.window, color=color, start_pos=start_pos, end_pos=end_pos, width=width)

    def reset_display(self):
        self.window.fill((0, 0, 0))
        self.draw_grid()
        self.draw_value()
        self.draw_lines()

    def is_cell_valid(self, x:int, y:int, value:str):
        if not value == " ":
            for i in range(self.GRID_LEN):
                # check column
                if self.grid[x][i].get_value() == value:
                    print(f"Value {value} is in column {x}")
                    return False
                # check row
                if self.grid[i][y].get_value() == value:
                    print(f"Value {value} is in row {y}")
                    return False
                # check 3x3 grid
                row = 3 * (x // 3) + i // 3
                col = 3 * (y // 3) + i % 3
                if self.grid[row][col].get_value() == value:
                    print(f"Value {value} is in 3x3 grid")
                    return False
        return True
