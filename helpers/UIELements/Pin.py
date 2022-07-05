from __future__ import annotations

from typing import Tuple
import pygame
from helpers.Assets import Assets

from helpers.Screen import Screen
from helpers.UIElement import UIElement


class Pin(UIElement):
    def __init__(self, screen: Screen, assets: Assets, position: Tuple, max_pin: int) -> None:
        """_summary_

        :param screen: Screen to draw the pin to
        :type screen: Screen
        :param assets: Assets file to pull assets from
        :type assets: Assets
        :param position: position to draw the pin to(top left corner)
        :type position: Tuple
        :param max_pin: maximum amount of pins in the game (6/7/8)
        :type max_pin: int
        """
        self.screen = screen
        self.assets = assets
        self.position = position
        self.max_pin = max_pin

        self.changed = False

        self.color_pos = -1
        self.position = (32 * position[0] + 25, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)
        self.border_rect = pygame.Rect(self.position[0] - 1, self.position[1] - 1, 26, 26)

    def next_color(self) -> None:
        """Changes to the next color
        """
        if self.changed:
            if self.color_pos + 1 == self.max_pin:
                self.color_pos = 0
            else:
                self.color_pos = self.color_pos + 1
        else:
            self.changed = True
            self.color_pos = 0
        self.color = self.assets.color_pins[self.color_pos]

    def previous_color(self) -> None:
        """Changes to the previous color
        """
        if self.changed:
            if self.color_pos - 1 == -1:
                self.color_pos = self.max_pin - 1
            else:
                self.color_pos = self.color_pos - 1
        else:
            self.changed = True
            self.color_pos = self.max_pin - 1
        self.color = self.assets.color_pins[self.color_pos]

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
        if self.changed:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.assets.gray, self.rect)

    def handle_events(self, events: pygame.EventList) -> None:
        """Handles events passed to this container in the screen also passes the events to all the items inside the container to check in their own handle events function and handle accordingly

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if event.button == 1:
                        self.next_color()
                    elif event.button == 3:
                        self.previous_color()
