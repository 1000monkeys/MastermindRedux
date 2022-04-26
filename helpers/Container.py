import sys

from helpers.UIElement import UIElement


class Container(UIElement):
    def __init__(self, pygame, screen, items: list, background_color, border_color, border_size) -> None:
        self.pygame = pygame
        self.screen = screen

        self.items = list()
        if items is not None:
            for item in items:
                self.items.append(item)

        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        
        self.min_position = (0, 0)
        self.max_position = (0, 0)
        self.get_min_position()
        self.get_max_position()
        print(self.max_position[0] - self.min_position[0])

    def get_min_position(self):
        self.min_position = (sys.maxsize, sys.maxsize)
        for item in self.items:
            if item.position[0] < self.min_position[0]:
                self.min_position = (item.position[0], self.min_position[1])
            if item.position[1] < self.min_position[1]:
                self.min_position = (self.min_position[0], item.position[1])

        self.background_rect = self.pygame.Rect(
            self.min_position,
            self.max_position
        )

    def get_max_position(self):
        self.max_position = (0, 0)
        for item in self.items:
            if item.position[0] > self.max_position[0]:
                self.max_position = (item.position[0] + item.text_rect[2], self.max_position[1])
            if item.position[1] > self.max_position[1]:
                self.max_position = (self.max_position[0], item.position[1] + item.text_rect[3])

        self.background_rect = self.pygame.Rect(
            self.min_position[0],
            self.min_position[1],
            self.max_position[0],
            self.max_position[1]
        )

    def add_item(self, item):
        self.items.append(item)

    def draw(self):
        self.screen.fill(self.background_color, self.background_rect)

        for item in self.items:
            item.draw()

    def check_events(self):
        pass
