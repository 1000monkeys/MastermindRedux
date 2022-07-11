from __future__ import annotations

import sys
from types import FunctionType
from typing import List, Tuple
from unittest.mock import call
import pygame
from helpers.Assets import Assets
from helpers.Screen import Screen
from helpers.UIElements.Button import Button
from helpers.UIElements.TextDisplay import TextDisplay
from helpers.UIElement import UIElement


class TextLoop(UIElement):
    def __init__(self, screen: Screen, assets: Assets, texts: str, position: Tuple, text_color: Tuple=(255, 255, 255), background_color: Tuple=None, border_color: Tuple=None, border_size: int=0, font_size: int=36, padding: int=0, callback_function: FunctionType=None) -> None:
        """This is a input type which has multiple set options, you loop through the by clicking on the existing text

        :param screen: The screen to draw the textloop to
        :type screen: Screen
        :param texts: Texts to loop through
        :type texts: str
        :param position: position to place the textloop, topleft corner
        :type position: Tuple
        :param text_color: Color of the text, defaults to (255, 255, 255)
        :type text_color: Tuple, optional
        :param background_color: Color of background behind the text, defaults to None
        :type background_color: Tuple, optional
        :param border_color: Color of the border around the text, defaults to None
        :type border_color: Tuple, optional
        :param border_size: size of the border around the text, defaults to 0
        :type border_size: int, optional
        :param font_size: Size of the text, defaults to 36
        :type font_size: int, optional
        :param padding: padding between text and border, defaults to 0
        :type padding: int, optional
        :param callback_function: function to call after the press, defaults to None
        :type callback_function: FunctionType, optional
        """
        self.screen = screen
        self.assets = assets
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

        rect = self.get_rect()
        self.left = Button(
            self.screen,
            assets=self.assets,
            text="<",
            position=(self.position[0], self.position[1] + 7),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_color=self.assets.black,
            border_size=3,
            font_size=18,
            padding=2,
            callback_function=self.previous_option
        )

        self.right = Button(
            self.screen,
            assets=self.assets,
            text=">",
            position=(self.position[0] + 25, self.position[1] + 7),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_color=self.assets.black,
            border_size=3,
            font_size=18,
            padding=2,
            callback_function=self.next_option
        )

    def previous_option(self) -> None:
        """Sets the option and text to the previous one or if there is no previous one to the last one
        """
        self.current_option = self.current_option - 1
        if self.current_option < 0:
            self.current_option = len(self.texts) - 1
        self.create_text_displays()
        if self.callback_function is not None:
            self.callback_function()

    def next_option(self) -> None:
        """Sets the option and text to the next one or if there is no next one to the first one
        """
        self.current_option = self.current_option + 1
        if self.current_option >= len(self.texts):
            self.current_option = 0
        self.create_text_displays()
        if self.callback_function is not None:
            self.callback_function()

    def get_text_displays(self) -> List:
        """Return the textdisplays that this textloops loops over

        :return: list of all text displays
        :rtype: List
        """
        return self.text_displays

    def create_text_displays(self) -> None:
        """Creates the text displays in a new list
        """
        self.text_displays = list()
        for i, text in enumerate(self.texts):
            self.text_displays.insert(i, TextDisplay(
                    screen=self.screen,
                    assets=self.assets,
                    text=text,
                    position=(self.position[0] + 50, self.position[1]),
                    text_color=self.text_color,
                    background_color=None,
                    border_color=None,
                    border_size=10,
                    font_size=self.font_size,
                    padding=self.padding
                )
            )
        self.get_rect()

    def get_option(self) -> int:
        """Returns the position value of the current option

        :return: The position of the current option
        :rtype: int
        """
        return self.current_option

    def set_option(self, option_pos: int) -> None:
        """Sets the current option to the passed option pos

        :param option_pos: The position of the option it should be set to
        :type option_pos: int
        """
        if option_pos < 0:
            return Exception("Option position lower than 0!")

        if option_pos > len(self.texts):
            return Exception("Option position higher than amount of options!")

        self.current_option = option_pos
        self.text_displays = list()
        self.create_text_displays()

    def get_rect(self) -> pygame.Rect:
        """Calculates the max rect size and returns this

        :return: Max size of rect of all possible options
        :rtype: pygame.Rect
        """
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
        """Handles events passed here from the screen

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)

        self.left.handle_events(events)
        self.right.handle_events(events)

    def draw(self):
        """Draw method usually called in the screen to draw the textinput
        """
        super().draw()

        self.left.draw()
        self.right.draw()
        self.text_displays[self.current_option].draw()
