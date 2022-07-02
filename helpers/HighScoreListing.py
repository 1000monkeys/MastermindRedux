from operator import index
from turtle import left
from helpers.Container import Container

from helpers.TextDisplay import TextDisplay

class HighScoreListing:
    def __init__(self, screen, left_text, right_text, position, text_color=(255, 255, 255), background_color=None, border_color=None, border_size=0, font_size=36, padding=0) -> None:
        self.screen = screen
        self.left_text = left_text
        self.right_text = right_text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.font_size = font_size
        self.padding = padding


        self.texts = dict()
        self.texts["left"] = TextDisplay(
            screen,
            text=self.left_text,
            position=position
        )
        self.texts["right"] = TextDisplay(
            screen,
            text=self.right_text,
            position=(position[0] + 800, position[1])
        )

        #self.merged_items = StaticFunctions.merge_dict(self.texts, self.text_loops, self.inner_buttons)
        self.container = Container(
            self.screen,
            self.texts,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=5,
            padding=5,
        )

    def get_rect(self):
        return self.container.rect

    def draw(self):
        self.container.draw()

    def handle_events(self, events):
        pass
