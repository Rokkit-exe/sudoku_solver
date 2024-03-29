import pygame
import sys
from typing import List
from cell import Cell
from button import Button
from board import Board

# Initialize Pygame


# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
GRID_SIZE = 600
GRID_LEN = 9
CELL_SIZE = GRID_SIZE // GRID_LEN
CELL_CENTER = CELL_SIZE // 3
SPACE = 25
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 100

CLEAR_BUTTON_POS = (SPACE, GRID_SIZE + SPACE)
SOLVE_BUTTON_POS = (SPACE + BUTTON_WIDTH + SPACE, GRID_SIZE + SPACE)
CHECK_BUTTON_POS = (SPACE + BUTTON_WIDTH + SPACE + BUTTON_WIDTH + SPACE, GRID_SIZE + SPACE)



# Create the window



# valid sudoku board
board_value = [["5","3"," "," ","7"," "," "," "," "]
            ,["6"," "," ","1","9","5"," "," "," "]
            ,[" ","9","8"," "," "," "," ","6"," "]
            ,["8"," "," "," ","6"," "," "," ","3"]
            ,["4"," "," ","8"," ","3"," "," ","1"]
            ,["7"," "," "," ","2"," "," "," ","6"]
            ,[" ","6"," "," "," "," ","2","8"," "]
            ,[" "," "," ","4","1","9"," "," ","5"]
            ,[" "," "," "," ","8"," "," ","7","9"]]


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    board_font = pygame.font.Font(None, 48)
    button_font = pygame.font.Font(None, 32)
    pygame.display.set_caption("Sudoku")

    board = Board(window, board_font)
    board.init_grid(board_value)

    clear_button = Button(
        CLEAR_BUTTON_POS[0], 
        CLEAR_BUTTON_POS[1], 
        BUTTON_WIDTH, 
        BUTTON_HEIGHT, 
        "Clear", 
        (0, 0, 255), 
        button_font)
    
    solve_button = Button(
        SOLVE_BUTTON_POS[0], 
        SOLVE_BUTTON_POS[1], 
        BUTTON_WIDTH, 
        BUTTON_HEIGHT, 
        "Solve", 
        (0, 0, 255), 
        button_font)
    
    check_button = Button(
        CHECK_BUTTON_POS[0], 
        CHECK_BUTTON_POS[1], 
        BUTTON_WIDTH, 
        BUTTON_HEIGHT, 
        "Check", 
        (0, 0, 255), 
        button_font)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse.
                pos = pygame.mouse.get_pos()
                if clear_button.get_rect().collidepoint(pos):
                    print("Clear button clicked")
                    board.init_grid(board_value)
                    board.reset_display()
                elif solve_button.get_rect().collidepoint(pos):
                    print("Solve button clicked")
                    board.init_grid(board_value)
                elif check_button.get_rect().collidepoint(pos):
                    print("Check button clicked")
                    board.init_grid(board_value)
                elif board.rect.collidepoint(pos):
                    # Calculate the cell coordinates by dividing by the cell size.
                    cell_x, cell_y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    print(f"Cell clicked: ({cell_x}, {cell_y})")
                    board.deselect_all()
                    board.grid[cell_x][cell_y].select()
            elif event.type == pygame.KEYDOWN:
                index = board.find_selected()
                if index:
                    if Cell.is_value_valid(event.unicode) and not board.grid[index[0]][index[1]].is_read_only:
                        if board.is_cell_valid(index[0], index[1], event.unicode):
                            print(f"Value entered: {event.unicode} is valid")
                            board.grid[index[0]][index[1]].set_value(event.unicode)
                            board.grid[index[0]][index[1]].deselect()
                            board.reset_display()
                            clear_button.draw(window)
                            solve_button.draw(window)
                            check_button.draw(window)
                        else:
                            print(f"Value entered: {event.unicode} is invalid")
            else:
                board.draw_grid()
                board.draw_value()
                board.draw_lines()
        clear_button.draw(window)
        solve_button.draw(window)
        check_button.draw(window)

        pygame.display.update()