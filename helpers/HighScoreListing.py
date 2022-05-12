from operator import index
from typing import Container

class HighScoreListing:
    def __init__(self, screen, left_text, right_text, text_color=(255, 255, 255), background_color=None, border_color=None, border_size=0, font_size=36, padding=0) -> None:
        self.screen = screen
        self.left_text = left_text
        self.right_text = right_text
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.font_size = font_size
        self.padding = padding

    
        # self.container = Container(
        #     screen,
        #     ITEMS,
        #     self.background_color,
        #     self.border_color,
        #     self.border_size,
        #     self.padding
        # )

    def draw():
        pass

