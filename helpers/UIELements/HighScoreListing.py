from typing import Tuple

import pygame
from helpers.UIELements.Container import Container
from helpers.Screen import Screen

from helpers.UIELements.TextDisplay import TextDisplay
from helpers.UIElement import UIElement

class HighScoreListing(UIElement):
    def __init__(self, screen: Screen, left_text: str, right_text: str, position: Tuple, text_color: Tuple=(255, 255, 255), background_color: Tuple=None, border_color: Tuple=None, border_size: int=0, font_size: int=36, padding: int=0) -> None:
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

    def get_rect(self) -> pygame.Rect:
        return self.container.rect

    def draw(self) -> None:
        super().draw()

        self.container.draw()

    def handle_events(self, events) -> None:
        super().handle_events(events)
