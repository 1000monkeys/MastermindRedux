from typing import Tuple
import pygame
from helpers.Screen import Screen

from helpers.UIElement import UIElement


class TextInput(UIElement):
    def __init__(self, screen: Screen, text: str, position: Tuple, text_color: str, background_color: Tuple=None, border_color: Tuple=None, border_width: int=None, max: int=None):
        self.screen = screen
        self.text = text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.max = max

        self.changed_text = False
        self.font = pygame.font.SysFont("arial", 48)
        width, height = self.font.size(self.text)
        if self.border_color != None and self.border_width != None:
            self.border_rect = pygame.Rect(
                self.position[0] - self.border_width,
                self.position[1] - self.border_width,
                width + 20 + self.border_width * 2,
                height + self.border_width * 2
            )
        self.rect = pygame.Rect(self.position[0], self.position[1], width + 20, height)
        
        self.background_color = background_color

    def get_rect(self) -> pygame.Rect:
        if self.border_color != None and self.border_width != None:
            return self.border_rect
        else:
            return self.rect

    def get_input(self) -> str:
        return self.text

    def set_input(self, text: str) -> None:
        self.text = text

    def draw(self):
        super().draw()

        self.update_size()

        if self.border_color != None and self.border_width != None:
            pygame.draw.rect(self.screen, self.border_color, self.border_rect)
        
        if self.background_color != None:
            pygame.draw.rect(self.screen, self.background_color, self.rect)

        text_img = self.font.render(self.text, False, self.text_color)
        self.screen.blit(text_img, (self.rect.x + 10, self.rect.y))

    def handle_events(self, events) -> None:
        super().handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if not self.changed_text:
                        self.changed_text = True
                        self.text = str()
                    else:
                        self.text = self.text[:-1]
                elif event.key:
                    if event.unicode.isalpha() and len(self.text) < self.max:
                        if not self.changed_text:
                            self.changed_text = True
                            self.text = str(event.unicode)
                        else:
                            self.text += event.unicode

    def update_size(self) -> None:
        width, height = self.font.size(self.text)
        if self.border_color != None and self.border_width != None:
            self.border_rect = pygame.Rect(
                self.position[0] - self.border_width,
                self.position[1] - self.border_width,
                width + 20 + self.border_width * 2,
                height + self.border_width * 2
            )
        self.rect = pygame.Rect(self.position[0], self.position[1], width + 20, height)