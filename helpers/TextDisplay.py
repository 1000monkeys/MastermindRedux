import pygame

from helpers.UIElement import UIElement

class TextDisplay(UIElement):
    def __init__(self, screen, text, position, text_color=(255, 255, 255), background_color=None, border_color=None, font_size=36, padding=0) -> None:
        self.screen = screen
        self.text = text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.padding = padding
        self.font_size = font_size

        self.font = pygame.font.SysFont("arial", self.font_size)
        self.font_width, self.font_height = self.font.size(text)

        if border_color is not None:
            self.border_rect = pygame.Rect(
                self.position[0] - self.padding * 2,
                self.position[1] - self.padding * 2,
                self.font_width + self.padding * 4, # border 4 padding steps
                self.font_height + self.padding * 4
            )

        self.rect = pygame.Rect(
            self.position[0] - self.padding,
            self.position[1] - self.padding,
            self.font_width + self.padding * 2, # inner rect
            self.font_height + self.padding * 2
        )

        self.text_rendered = self.font.render(
            text,
            True,
            self.text_color,
            self.background_color,
        )
        self.text_rect = self.text_rendered.get_rect(center=(self.rect.center))

    def get_rect(self):
        return self.rect

    def draw(self):
        if self.border_color is not None:
            self.screen.fill(self.border_color, self.border_rect)
        if self.background_color is not None:
            self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.text_rendered, self.text_rect)

    def handle_events(self):
        pass