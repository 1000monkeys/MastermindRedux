from __future__ import annotations

from typing import Tuple
import pygame
from helpers.Assets import Assets
from helpers.Screen import Screen

from helpers.UIElement import UIElement


class ResultPin(UIElement):
    def __init__(self, screen: Screen, assets: Assets, position: Tuple) -> None:
        """_summary_

        :param screen: Screen to draw the result pin to
        :type screen: Screen
        :param assets: Assets file containing assets to be used in this class
        :type assets: Assets
        :param position: position of the resultpin(top left corner)
        :type position: Tuple
        """
        self.screen = screen
        self.assets = assets
        self.position = position

        self.color = self.assets.gray

        self.position = (32 * position[0] + 300, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)
        self.border_rect = pygame.Rect(self.position[0] - 1, self.position[1] - 1, 26, 26)

    def set_black(self) -> None:
        """Set's the result pin to black
        """
        self.color = self.assets.black

    def set_white(self) -> None:
        """Set's the result pin to white
        """
        self.color = self.assets.white

    def get_rect(self) -> pygame.Rect:
        """Returns the rect which contains the position and size of the button. The background rect.

        :return: position dictionary with 4 values, first 2 being X/Y and next 2 being width/height
        :rtype: pygame.Rect
        """
        return self.rect

    def draw(self) -> None:
        """Draw method called from the screen
        """
        super().draw()

        pygame.draw.rect(self.screen, self.assets.black, self.border_rect)        
        pygame.draw.rect(self.screen, self.color, self.rect)

    def handle_events(self, events: pygame.EventList) -> None:
        """Handles events passed to this container in the screen also passes the events to all the items inside the container to check in their own handle events function and handle accordingly

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)
