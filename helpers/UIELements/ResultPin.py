from typing import Tuple
import pygame
from helpers.Assets import Assets
from helpers.Screen import Screen

from helpers.UIElement import UIElement


class ResultPin(UIElement):
    def __init__(self, screen: Screen, assets: Assets, position: Tuple) -> None:
        self.screen = screen
        self.assets = assets
        self.position = position

        self.color = self.assets.gray

        self.position = (32 * position[0] + 300, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)
        self.border_rect = pygame.Rect(self.position[0] - 1, self.position[1] - 1, 26, 26)

    def set_black(self) -> None:
        self.color = self.assets.black

    def set_white(self) -> None :
        self.color = self.assets.white

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def draw(self) -> None:
        super().draw()

        pygame.draw.rect(self.screen, self.assets.black, self.border_rect)        
        pygame.draw.rect(self.screen, self.color, self.rect)

    def handle_events(self, events) -> None:
        super().handle_events(events)
