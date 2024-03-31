import pygame
import sys
from typing import List
from cell import Cell
from button import Button
from board import Board
from color import Color

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
GRID_SIZE = 600
SPACE = 25
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 100

CLEAR_BUTTON_POS = (SPACE, GRID_SIZE + SPACE)
SOLVE_BUTTON_POS = (SPACE + BUTTON_WIDTH + SPACE, GRID_SIZE + SPACE)
CHECK_BUTTON_POS = (SPACE + BUTTON_WIDTH + SPACE + BUTTON_WIDTH + SPACE, GRID_SIZE + SPACE)

# valid sudoku board
board_value = [[" ","3","1","2"," "," "," ","6","9"]
            ,[" "," ","2"," ","8","4"," ","5"," "]
            ,["5"," ","9","6"," "," "," "," "," "]
            ,["3","9","6","7","4","5","1"," "," "]
            ,["1"," ","7","8"," "," "," "," "," "]
            ,["2","8"," "," "," ","6","5"," ","3"]
            ,["4","1"," ","3"," "," ","6"," "," "]
            ,["7"," "," ","4","2"," "," "," ","5"]
            ,[" "," ","8"," "," "," "," ","3","4"]]


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
        Color.BLUE.value, 
        button_font)
    
    solve_button = Button(
        SOLVE_BUTTON_POS[0], 
        SOLVE_BUTTON_POS[1], 
        BUTTON_WIDTH, 
        BUTTON_HEIGHT, 
        "Solve", 
        Color.BLUE.value, 
        button_font)
    
    check_button = Button(
        CHECK_BUTTON_POS[0], 
        CHECK_BUTTON_POS[1], 
        BUTTON_WIDTH, 
        BUTTON_HEIGHT, 
        "Check", 
        Color.BLUE.value, 
        button_font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            clear_button.handle_click(event, board.init_grid, board_value)
            solve_button.handle_click(event, board.start_solve_board)
            check_button.handle_click(event, board.verify_board, check_button)
            board.handle_click(event)
            board.handle_keydown(event)    
            
        board.draw_grid()
        board.draw_value()
        board.draw_lines()
        clear_button.draw(window)
        solve_button.draw(window)
        check_button.draw(window)

        pygame.display.update()