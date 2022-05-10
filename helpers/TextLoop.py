import pygame
from helpers.TextDisplay import TextDisplay


class TextLoop:
    def __init__(self, screen, texts, position, text_color=(255, 255, 255), background_color=None, border_color=None, font_size=36, padding=0) -> None:
        self.screen = screen
        self.texts = texts
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.padding = padding
        self.font_size = font_size

        self.current_option = 0

        self.text_display = TextDisplay(
            self.screen,
            self.texts[self.current_option],
            self.position,
            self.text_color,
            self.background_color,
            self.border_color,
            self.font_size,
            self.padding
        )

    def next_option(self):
        self.current_option = self.current_option + 1
        if self.current_option >= len(self.texts):
            self.current_option = 0

        self.text_display = TextDisplay(
            self.screen,
            self.texts[self.current_option],
            self.position,
            self.text_color,
            self.background_color,
            self.border_color,
            self.font_size,
            self.padding
        )

    def get_option(self):
        return self.current_option

    def set_option(self, option_pos):
        if option_pos < 0:
            return Exception("Option position lower than 0!")

        if option_pos > len(self.texts):
            return Exception("Option position higher than amount of options!")

        self.current_option = option_pos

        self.text_display = TextDisplay(
            self.screen,
            self.texts[self.current_option],
            self.position,
            self.text_color,
            self.background_color,
            self.border_color,
            self.font_size,
            self.padding
        )

    def get_rect(self):
        return self.text_display.get_rect()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.text_display.get_rect().collidepoint(event.pos):
                    self.next_option()

    def draw(self):
        self.text_display.draw()
