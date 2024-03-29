import pygame
import sys

class Cell():
    def __init__(self, x:int, y:int, size:int, value:str, rect:pygame.Rect):
        self.__SIZE = size
        self.__CENTER = size // 3
        self.__x = x
        self.__y = y
        self.__pos_x = x*size
        self.__pos_y = y*size
        self.__rect = rect
        self.__value = value
        self.__color = (255, 255, 255)
        self.__font_color = (0, 128, 0)
        self.__is_selected = False
        self.is_read_only = True

        if self.__value == " ":
            self.__font_color = (255, 255, 255)
            self.is_read_only = False
        
    @staticmethod
    def is_value_valid(value:str):
        return value in "123456789 "
    

    def __str__(self):
        return f"({self.__x}, {self.__y}) = {self.__value}"
    
    def get_value(self):
        return self.__value
    
    def get_position(self):
        return self.__x, self.__y
    
    def get_size(self):
        return self.__SIZE
    
    def is_selected(self):
        return self.__is_selected
    
    def set_value(self, value:str):
        self.__value = value

    def set_color(self, color:tuple):
        self.__color = color

    def draw_rect(self, window:pygame.Surface, width:int=1):
        pygame.draw.rect(
            surface=window, 
            color=self.__color, 
            rect=self.__rect, 
            width=width
        )

    def select(self):
        self.__is_selected = True
        self.__color = (255, 0, 0)

    def deselect(self):
        self.__is_selected = False
        self.__color = (255, 255, 255)
    
    def draw_value(self, window: pygame.Surface, font:pygame.font.Font):
        text = font.render(self.__value, True, self.__font_color)
        window.blit(text, (self.__pos_x+self.__CENTER, self.__pos_y + self.__CENTER))

    def reset_value(self, window: pygame.Surface):
        self.set_color((255, 255, 255))
        self.draw_rect(window, 1)

    def is_clicked(self, pos):
        x, y = pos
        return self.__x == x and self.__y == y