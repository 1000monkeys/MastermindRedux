from __future__ import annotations

import sys
from types import FunctionType
from typing import List, Tuple
import pygame
from helpers.Screen import Screen
from helpers.UIElements.TextDisplay import TextDisplay
from helpers.UIElement import UIElement


class TextLoop(UIElement):
    def __init__(self, screen: Screen, texts: str, position: Tuple, text_color: Tuple=(255, 255, 255), background_color: Tuple=None, border_color: Tuple=None, border_size: int=0, font_size: int=36, padding: int=0, callback_function: FunctionType=None) -> None:
        self.screen = screen
        self.texts = texts
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.padding = padding
        self.font_size = font_size
        self.callback_function = callback_function

        self.current_option = 0
        self.text_displays = list()
        self.create_text_displays()

    def next_option(self) -> None:
        self.current_option = self.current_option + 1
        if self.current_option >= len(self.texts):
            self.current_option = 0
        self.text_displays = list()
        self.create_text_displays()

    def get_text_displays(self) -> List:
        return self.text_displays

    def create_text_displays(self) -> None:
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

    def get_option(self) -> int:
        return self.current_option

    def set_option(self, option_pos: int) -> None:
        if option_pos < 0:
            return Exception("Option position lower than 0!")

        if option_pos > len(self.texts):
            return Exception("Option position higher than amount of options!")

        self.current_option = option_pos
        self.text_displays = list()
        self.create_text_displays()

    def get_rect(self) -> pygame.Rect:
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

    def handle_events(self, events: pygame.EventList):
        super().handle_events(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.callback_function is not None:
                    if self.text_displays[self.current_option].rect.collidepoint(event.pos):
                        self.next_option()
                        self.callback_function()
                elif self.text_displays[self.current_option].rect.collidepoint(event.pos):
                    self.next_option()

    def draw(self):
        super().draw()

        self.text_displays[self.current_option].draw()
