from typing import Tuple
import pygame
from helpers.Assets import Assets

from helpers.Screen import Screen
from helpers.UIElement import UIElement


class Pin(UIElement):
    def __init__(self, screen: Screen, assets: Assets, position: Tuple, max_pin: int) -> None:
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
        return self.rect

    def draw(self) -> None:
        super().draw()

        pygame.draw.rect(self.screen, self.assets.black, self.border_rect)
        if self.changed:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.assets.gray, self.rect)

    def handle_events(self, events) -> None:
        super().handle_events(events)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if event.button == 1:
                        self.next_color()
                    elif event.button == 3:
                        self.previous_color()
