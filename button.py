import pygame
from typing import Callable, Any, Tuple
from color import Color


class Button():
    def __init__(self, x:int, y:int, width:int, height:int, text:str, color:tuple, font:pygame.font.Font):
        self._x: int = x
        self._y: int = y
        self._width: int = width
        self._height: int = height
        self._text: str = text
        self._color: Tuple[int, int, int] = color
        self._font: pygame.font.Font = font
        self._rect: pygame.Rect = pygame.Rect(x, y, width, height)

    @property
    def pos(self) -> tuple[int, int]:
        return self._x, self._y
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, text:str) -> None:
        self._text = text
    
    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color
    
    @color.setter
    def color(self, color: Tuple[int, int, int]) -> None:
        self._color = color
    
    @property
    def font(self) -> pygame.font.Font:
        return self._font

    @property
    def rect(self) -> pygame.Rect:
        return self._rect
    

    def draw(self, window:pygame.Surface):
        """
        Draws the button rectangle and the font on the surface passed in params.
        """
        pygame.draw.rect(window, self._color, self._rect)
        text = self._font.render(self._text, True, Color.WHITE.value)
        text_rect = text.get_rect(center=self._rect.center)
        window.blit(text, text_rect)

    def handle_click(self, event: pygame.event, func: Callable, *args: Any):
        """
        Handles a click event.

        Parameters:
        event (pygame.Event): The event to handle.
        func (function): The function to call when the button is clicked.
        *args: Additional arguments to pass to the function.

        Returns:
        None
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self._rect.collidepoint(pos):
                func(*args)

