from itertools import count
from operator import index, indexOf
import pygame
from helpers.Screen import Screen
from screens.MainMenu import MainMenu
from screens.Settings import Settings

class DisplayManager:
    def __init__(self, pygame, screen) -> None:
        self.screen = screen
        self.screen_id = 0
        self.screens = [
            MainMenu(pygame, screen, self),
            Settings(pygame, screen, self)
        ]

    def get_current_screen(self):
        return self.screens[self.screen_id]

    def change_screen(self, screen_class):
        counter = 0
        for screen in self.screens:
            if screen.__class__ == screen_class:
                self.screen_id = counter
                break
            counter = counter + 1
