import sys
from xml.dom.minicompat import EmptyNodeList
import pygame
from helpers.UIElement import UIElement


class Container(UIElement):
    def __init__(self, screen, items: list, background_color, border_color, border_size, padding) -> None:
        self.screen = screen

        self.items = list()
        if items is not None:
            self.items = items
        elif items is None:
            self.items = list()

        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.padding = padding

        if len(self.items) > 0:
            self.max_position = (0, 0)
            self.min_position = (sys.maxsize, sys.maxsize)
            for item in self.items:
                if isinstance(item, type(Container)):
                    raise Exception("Cannot put a container in a container!")
                    
                if item.get_rect()[0] < self.min_position[1]:
                    self.min_position = (item.get_rect()[0], self.min_position[0])
                if item.get_rect()[1] < self.min_position[1]:
                    self.min_position = (self.min_position[0], item.get_rect()[1])

                if item.get_rect()[0] + item.get_rect()[2] > self.max_position[0]:
                    self.max_position = (item.get_rect()[0] + item.get_rect()[2], self.max_position[1])
                if item.get_rect()[1] + item.get_rect()[3] > self.max_position[1]:
                    self.max_position = (self.max_position[0], item.get_rect()[1] + item.get_rect()[3])

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

    def get_rect(self):
        return self.border_rect

    def draw(self):
        self.screen.fill(self.border_color, self.border_rect)
        self.screen.fill(self.background_color, self.rect)

        for item in self.items:
            item.draw()

    def handle_events(self):
        pass
