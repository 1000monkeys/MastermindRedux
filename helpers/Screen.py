import sys

import pygame

class Screen:
    def __init__(self) -> None:
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self):
        pass