import sys
from xml.dom.minicompat import EmptyNodeList
import pygame
from helpers.Button import Button
from helpers.TextLoop import TextLoop
from helpers.UIElement import UIElement


class Container(UIElement):
    def __init__(self, screen, items: list, background_color, border_color, border_size, padding) -> None:
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


    def calculate_size(self):
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
        

    def add_item(self, item):
        self.items.append(item)
        self.calculate_size()


    def get_rect(self):
        return self.border_rect


    def draw(self):
        self.screen.fill(self.border_color, self.border_rect)
        self.screen.fill(self.background_color, self.rect)

        for key in self.items.keys():
            self.items[key].draw()


    def handle_events(self):
        pass
