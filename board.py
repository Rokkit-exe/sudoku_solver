import pygame
from typing import List
from cell import Cell
from button import Button
from color import Color
import threading

class Board():
    def __init__(self, window:pygame.Surface, font:pygame.font.Font, grid_size:int=600 ):
        self._GRID_LEN = 9
        self._GRID_SIZE = grid_size
        self._CELL_SIZE = grid_size // self._GRID_LEN
        self._grid = [[None for _ in range(self._GRID_LEN)] for _ in range(self._GRID_LEN)]
        self._window = window
        self._font = font
        self._rect = pygame.Rect(0, 0, self._GRID_SIZE, self._GRID_SIZE)
        self._lock = threading.Lock()

    @property
    def grid(self) -> List[List[Cell]]:
        return self._grid
    
    @property
    def cell(self, x:int, y:int) -> Cell:
        return self._grid[x][y]


    def init_grid(self, board: List[List[str]]) -> None:
        self._grid = [[None for _ in range(self._GRID_LEN)] for _ in range(self._GRID_LEN)]
        for x in range(self._GRID_LEN):
            for y in range(self._GRID_LEN):
                print(f"({x}, {y}) = {board[x][y]}" )
                cell = Cell(x, y, self._CELL_SIZE, board[y][x], pygame.Rect(x*self._CELL_SIZE, y*self._CELL_SIZE, self._CELL_SIZE, self._CELL_SIZE))
                self._grid[x][y] = cell
        self.reset_display()
    
    def draw_grid(self) -> None:
        for x in range(len(self._grid[0])):
            for y in range(len(self._grid[1])):
                self._grid[x][y].draw_rect(self._window)

    def draw_value(self):
        for x in range(len(self._grid[0])):
            for y in range(len(self._grid[1])):
                self._grid[x][y].draw_value(self._window, self._font)

    def draw_lines(self, color: tuple=Color.BLUE.value, width: int=3):
        # vertical lines
        for i in range(3, self._GRID_LEN, 3):
            start_pos = (self._CELL_SIZE*i, 0)
            end_pos = (self._CELL_SIZE*i, self._GRID_SIZE)
            pygame.draw.line(surface=self._window, color=color, start_pos=start_pos, end_pos=end_pos, width=width)

        # horizontal lines
        # vertical lines
        for i in range(3, self._GRID_LEN, 3):
            start_pos = (0, self._CELL_SIZE*i)
            end_pos = (self._GRID_SIZE, self._CELL_SIZE*i)
            pygame.draw.line(surface=self._window, color=color, start_pos=start_pos, end_pos=end_pos, width=width)

    def deselect_all(self):
        for row in self._grid:
            for cell in row:
                cell.deselect()

    def find_selected_cell_pos(self) -> tuple[int, int]:
        for row in self._grid:
            for cell in row:
                if cell.is_selected:
                    return cell.pos
        return None
    
    def print_board(self) -> None:
        for row in self._grid:
            for cell in row:
                print(cell.value, end=" ")
            print()
    
    def reset_display(self) -> None:
        self._window.fill((0, 0, 0))
        self.draw_grid()
        self.draw_value()
        self.draw_lines()
        pygame.display.update()

    def is_cell_valid(self, x:int, y:int, value:str) -> bool:
        if not value == " ":
            for i in range(self._GRID_LEN):
                # check column
                if self._grid[x][i].value == value:
                    print(f"Value {value} is in column {x}")
                    return False
                # check row
                if self._grid[i][y].value == value:
                    print(f"Value {value} is in row {y}")
                    return False
                # check 3x3 grid
                row = 3 * (x // 3) + i // 3
                col = 3 * (y // 3) + i % 3
                if self._grid[row][col].value == value:
                    print(f"Value {value} is in 3x3 grid")
                    return False
        return True
    
    def verify_board(self, button: Button) -> bool:
        print("Verifying board")
        for x in range(self._GRID_LEN):
            for y in range(self._GRID_LEN):
                if not self.is_cell_valid(x, y, self._grid[x][y].value):
                    print(f"Invalid board at {x}, {y}")
                    button.color = Color.RED.value
                    return False
        button.color = Color.GREEN.value
        print("Board is valid")        
    
    def start_solve_board(self) -> None:
        thread = threading.Thread(target=self.solve_board)
        thread.start()
        thread.join()
    
    def solve_board(self) -> bool:
        for x in range(self._GRID_LEN):
            for y in range(self._GRID_LEN):
                if self._grid[x][y].value == " ":
                    for value in "123456789":
                        if self.is_cell_valid(x, y, value):
                            with self._lock:
                                self._grid[x][y].set_value(value)
                                self.reset_display()
                            pygame.time.delay(100)
                            if self.solve_board():
                                return True
                            with self._lock:
                                self._grid[x][y].set_value(" ")
                                self.reset_display()
                            pygame.time.delay(100)
                    return False
        return True
        
    def handle_click(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self._rect.collidepoint(pos):
                # Calculate the cell coordinates by dividing by the cell size.
                cell_x, cell_y = pos[0] // self._CELL_SIZE, pos[1] // self._CELL_SIZE
                self.deselect_all()
                self._grid[cell_x][cell_y].select()

    def get_cell(self, x:int, y:int) -> Cell:
        return self._grid[x][y]

    def handle_keydown(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            pos = self.find_selected_cell_pos()
            if pos:
                if Cell.is_value_allowed(event.unicode) and not self._grid[pos[0]][pos[1]].is_read_only:
                    if self.is_cell_valid(pos[0], pos[1], event.unicode):
                        self._grid[pos[0]][pos[1]].set_value(event.unicode)
                        self._grid[pos[0]][pos[1]].deselect()
                        self.reset_display()
