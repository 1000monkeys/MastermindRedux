from __future__ import annotations

from typing import Tuple

import pygame
from helpers.Assets import Assets
from helpers.UIElements.Container import Container
from helpers.Screen import Screen

from helpers.UIElements.TextDisplay import TextDisplay
from helpers.UIElement import UIElement

class HighScoreListing(UIElement):
    def __init__(self, screen: Screen, assets: Assets, left_text: str, right_text: str, position: Tuple, text_color: Tuple=(255, 255, 255), background_color: Tuple=None, border_color: Tuple=None, border_size: int=0, font_size: int=36, padding: int=0) -> None:
        """Initialized the highscore listing with the needed data

        :param screen: Screen to draw to
        :type screen: Screen
        :param left_text: Text(name usually) on the left of the high score listing
        :type left_text: str
        :param right_text: Text(score usually) on the right of the high score listing
        :type right_text: str
        :param position: Position of the listing ( top left corner)
        :type position: Tuple
        :param text_color: Color of the text, RGB Value, defaults to (255, 255, 255)
        :type text_color: Tuple, optional
        :param background_color: Background color behind the text, RGB value, defaults to None
        :type background_color: Tuple, optional
        :param border_color: Border around the background, RGB Value, defaults to None
        :type border_color: Tuple, optional
        :param border_size: Size of the border, defaults to 0
        :type border_size: int, optional
        :param font_size: Text size, defaults to 36
        :type font_size: int, optional
        :param padding: Padding inside the background between the border and the text, defaults to 0
        :type padding: int, optional
        """
        self.screen = screen
        self.assets = assets
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
            assets=self.assets,
            text=self.left_text,
            position=position
        )
        self.texts["right"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.right_text,
            position=(position[0] + 800, position[1])
        )

        #self.merged_items = StaticFunctions.merge_dict(self.texts, self.text_loops, self.inner_buttons)
        self.container = Container(
            self.screen,
            assets=self.assets,
            items=self.texts,
            background_color=self.assets.brown,
            border_color=self.assets.white,
            border_size=5,
            padding=5,
        )

    def get_rect(self) -> pygame.Rect:
        """Returns the rect which contains the position and size of the button. The background rect.

        :return: position dictionary with 4 values, first 2 being X/Y and next 2 being width/height
        :rtype: pygame.Rect
        """
        return self.container.rect

    def draw(self) -> None:
        """Draw method called from the screen
        """
        super().draw()

        self.container.draw()

    def handle_events(self, events: pygame.EventList) -> None:
        """Handles events passed to this container in the screen also passes the events to all the items inside the container to check in their own handle events function and handle accordingly

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)
