import pygame

from helpers.UIElement import UIElement

class Button(UIElement):
    def __init__(self, screen, text, position, text_color, background_color=None, border_color=None, border_size=0, font_size=36, padding=0, callback_function=None) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_Color = border_color
        self.border_size = border_size
        self.font_size = font_size
        self.padding = padding
        self.callback_function = callback_function

        self.font = pygame.font.SysFont("arial", self.font_size)
        self.font_width, self.font_height = self.font.size(self.text)

        self.normal_rect = pygame.Rect(
            self.position[0],
            self.position[1],
            self.font_width + self.padding * 2,
            self.font_height + self.padding * 2
        )
        self.normal_border_rect = pygame.Rect(
            self.position[0] - self.padding - self.border_size,
            self.position[1] - self.padding - self.border_size,
            self.font_width + self.padding * 4 + self.border_size * 2,
            self.font_height + self.padding * 4 + self.border_size * 2
        )

        self.larger_rect = pygame.Rect(
            self.position[0] - self.padding * 2,
            self.position[1] - self.padding * 2,
            self.font_width + self.padding * 6,
            self.font_height + self.padding * 6
        )
        self.larger_border_rect = pygame.Rect(
            self.position[0] - self.padding * 3 - self.border_size,
            self.position[1] - self.padding * 3 - self.border_size,
            self.font_width + self.padding * 8 + self.border_size * 2,
            self.font_height + self.padding * 8 + self.border_size * 2
        )

        self.text_rendered = self.font.render(
            self.text,
            True,
            self.text_color,
            self.background_color
        )
        
        self.rect = self.normal_rect
        self.border_rect = self.normal_border_rect
        self.text_rect = self.text_rendered.get_rect()
        self.text_rect.center = self.normal_rect.center

    def get_rect(self):
        return self.rect

    def draw(self):
        self.screen.fill(self.text_color, self.border_rect)
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.text_rendered, self.text_rect)

    """
    pass events from the screen into this function to handle button specific behaviour
    """
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.border_rect.collidepoint(event.pos):
                    self.border_rect = self.larger_border_rect
                    self.rect = self.larger_rect

                    self.text_rect = self.text_rendered.get_rect()
                    self.text_rect.center = self.border_rect.center
                else:
                    self.border_rect = self.normal_border_rect
                    self.rect = self.normal_rect

                    self.text_rect = self.text_rendered.get_rect()
                    self.text_rect.center = self.border_rect.center

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.callback_function is not None:
                    if self.border_rect.collidepoint(event.pos):
                        self.callback_function()
