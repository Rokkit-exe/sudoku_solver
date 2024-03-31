import pygame
from color import Color

class Cell():
    def __init__(self, x:int, y:int, size:int, value:str, rect:pygame.Rect):
        self._CENTER = size // 3
        self._x = x
        self._y = y
        self._pos_x = x*size
        self._pos_y = y*size
        self._rect = rect
        self._value = value
        self._color = Color.WHITE.value
        self._font_color = (0, 128, 0)
        self._is_selected = False
        self._is_read_only = True

        if self._value == " ":
            self._font_color = Color.WHITE.value
            self._is_read_only = False

    def __str__(self) -> str:
        return f"({self._x}, {self._y}) = {self._value}"
        
    @property
    def value(self) -> str:
        return self._value
    
    @property
    def pos(self) -> tuple[int, int]:
        return self._x, self._y
    
    @property
    def is_selected(self) -> bool:
        return self._is_selected
    
    @property
    def is_read_only(self) -> bool:
        return self._is_read_only
    
    @staticmethod
    def is_value_allowed(value:str) -> bool:
        return value in "123456789 "
    
    def set_value(self, value:str) -> None:
        self._value = value

    def draw_rect(self, window:pygame.Surface, width:int=1) -> None:
        pygame.draw.rect(
            surface=window, 
            color=self._color, 
            rect=self._rect, 
            width=width
        )

    def draw_value(self, window: pygame.Surface, font:pygame.font.Font) -> None:
        text = font.render(self._value, True, self._font_color)
        window.blit(text, (self._pos_x+self._CENTER, self._pos_y + self._CENTER))

    def select(self) -> None:
        self._is_selected = True
        self._color = Color.RED.value

    def deselect(self) -> None:
        self._is_selected = False
        self._color = Color.WHITE.value
