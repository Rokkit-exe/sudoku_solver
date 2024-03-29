import pygame

class Button():
    def __init__(self, x:int, y:int, width:int, height:int, text:str, color:tuple, font:pygame.font.Font):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__color = color
        self.__font = font
        self.__rect = pygame.Rect(x, y, width, height)

    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, self.__color, self.__rect)
        text = self.__font.render(self.__text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.__rect.center)
        window.blit(text, text_rect)

    def set_color(self, color:tuple):
        self.__color = color

    def get_text(self):
        return self.__text

    def set_text(self, text:str):
        self.__text = text

    def get_rect(self):
        return self.__rect

    def click(self, func, *args):
        func(*args)
        
