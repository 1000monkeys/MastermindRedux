import sys
import pygame
from helpers.TextDisplay import TextDisplay


class TextLoop:
    def __init__(self, screen, texts, position, text_color=(255, 255, 255), background_color=None, border_color=None, border_size=0, font_size=36, padding=0) -> None:
        self.screen = screen
        self.texts = texts
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.padding = padding
        self.font_size = font_size

        self.current_option = 0
        self.text_displays = list()
        self.create_text_displays()

    def next_option(self):
        self.current_option = self.current_option + 1
        if self.current_option >= len(self.texts):
            self.current_option = 0
        self.create_text_displays()

    def get_text_displays(self):
        return self.text_displays

    def create_text_displays(self):
        border_size = 10
        for i, text in enumerate(self.texts):
            self.text_displays.insert(i, TextDisplay(
                    screen=self.screen,
                    text=text,
                    position=self.position,
                    text_color=self.text_color,
                    background_color=None,
                    border_color=None,
                    border_size=10,
                    font_size=self.font_size,
                    padding=self.padding
                )
            )

    def get_option(self):
        return self.current_option

    def set_option(self, option_pos):
        if option_pos < 0:
            return Exception("Option position lower than 0!")

        if option_pos > len(self.texts):
            return Exception("Option position higher than amount of options!")

        self.current_option = option_pos
        self.create_text_displays()

    def get_rect(self):
        self.max_position = (0, 0)
        self.min_position = (sys.maxsize, sys.maxsize)
        for text_display in self.text_displays:
            if text_display.get_rect()[0] < self.min_position[1]:
                self.min_position = (text_display.get_rect()[0], self.min_position[0])
            if text_display.get_rect()[1] < self.min_position[1]:
                self.min_position = (self.min_position[0], text_display.get_rect()[1])

            if text_display.get_rect()[0] + text_display.get_rect()[2] > self.max_position[0]: # width
                self.max_position = (text_display.get_rect()[0] + text_display.get_rect()[2], self.max_position[1])
            if text_display.get_rect()[1] + text_display.get_rect()[3] > self.max_position[1]: # height
                self.max_position = (self.max_position[0], text_display.get_rect()[1] + text_display.get_rect()[3])

        self.rect = pygame.Rect(
            self.min_position[0] - self.padding,
            self.min_position[1] - self.padding,
            self.max_position[0] - self.min_position[0] + self.padding * 2,
            self.max_position[1] - self.min_position[1] + self.padding * 2
        )

        return self.rect

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.text_displays[self.current_option].get_rect().collidepoint(event.pos):
                    self.next_option()

    def draw(self):
        self.text_displays[self.current_option].draw()
