from __future__ import annotations
import sys
from typing import Tuple
import pygame
from helpers.Screen import Screen
from helpers.UIElement import UIElement


class Container(UIElement):
    def __init__(self, screen: Screen, items: list, background_color: Tuple, border_color: Tuple, border_size: Tuple, padding: int) -> None:
        """This function initializes the container

        :param screen: The screen to draw the border, background and items to
        :type screen: Screen
        :param items: The items inside this container
        :type items: list
        :param background_color: The color behind the items filling the entire container
        :type background_color: Tuple
        :param border_color: The color around the background color making the border
        :type border_color: Tuple
        :param border_size: The size of the border around the container
        :type border_size: Tuple
        :param padding: The amount of padding inside the container between the contents and the border
        :type padding: int
        """
        self.screen = screen

        self.items = list()
        if items is not None:
            self.items = items
        elif items is None:
            self.items = dict()

        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.padding = padding
        self.calculate_size()


    def calculate_size(self) -> None:
        """Calculates the size of the container

        :raises Exception: Container in container
        :raises Exception: Empty container
        """
        if len(self.items) > 0:
            self.max_position = (0, 0)
            self.min_position = (sys.maxsize, sys.maxsize)
            for key in self.items.keys():
                if isinstance(self.items[key], type(Container)):
                    raise Exception("Cannot put a container in a container!")
                else:
                    if self.items[key].get_rect()[0] < self.min_position[0]:
                        self.min_position = (self.items[key].get_rect()[0], self.min_position[1])
                    if self.items[key].get_rect()[1] < self.min_position[1]:
                        self.min_position = (self.min_position[0], self.items[key].get_rect()[1])

                    if self.items[key].get_rect()[0] + self.items[key].get_rect()[2] > self.max_position[0]: # width
                        self.max_position = (self.items[key].get_rect()[0] + self.items[key].get_rect()[2], self.max_position[1])
                    if self.items[key].get_rect()[1] + self.items[key].get_rect()[3] > self.max_position[1]: # height
                        self.max_position = (self.max_position[0], self.items[key].get_rect()[1] + self.items[key].get_rect()[3])

            self.border_rect = pygame.Rect(
                self.min_position[0] - self.border_size - self.padding,
                self.min_position[1] - self.border_size - self.padding,
                self.max_position[0] - self.min_position[0] + self.border_size * 2 + self.padding * 2,
                self.max_position[1] - self.min_position[1] + self.border_size * 2 + self.padding * 2,
            )

            self.rect = pygame.Rect(
                self.min_position[0] - self.padding,
                self.min_position[1] - self.padding,
                self.max_position[0] - self.min_position[0] + self.padding * 2,
                self.max_position[1] - self.min_position[1] + self.padding * 2
            )
        else:
            raise Exception('Cannot have an empty container!')
        

    def add_item(self, item: UIElement) -> None:
        """Adds an item to the container

        :param item: Item to be added
        :type item: UIElement
        """
        self.items.append(item)
        self.calculate_size()

    def get_rect(self) -> pygame.Rect:
        """Get's the size and position of the container. The outer rect/border rect

        :return: position dictionary with 4 values, first 2 being X/Y and next 2 being width/height
        :rtype: pygame.Rect
        """
        return self.border_rect

    def draw(self) -> None:
        """Function that draws the border and background of the container to the passed screen variable
        Also draws all items to the passed screen variable
        """
        super().draw()

        self.screen.fill(self.border_color, self.border_rect)
        self.screen.fill(self.background_color, self.rect)

        for key in self.items.keys():
            self.items[key].draw()

    def handle_events(self, events: pygame.EventList) -> None:
        """Handles events passed to this container in the screen also passes the events to all the items inside the container to check in their own handle events function and handle accordingly

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)

        for key in self.items.keys():
            self.items[key].handle_events(events)
