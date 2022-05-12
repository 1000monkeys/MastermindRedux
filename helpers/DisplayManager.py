from itertools import count
from operator import index, indexOf
import pygame
from helpers.Screen import Screen
from screens.MainMenu import MainMenu
from screens.Settings import Settings
from screens.HighScore import HighScore

class DisplayManager:
    def __init__(self, pygame, screen) -> None:
        self.screen = screen
        self.screen_id = 0

        # Screen type to screen_id
        self.screens = list()
        self.screens.insert(0, MainMenu(pygame, screen, self))
        self.screens.insert(1, Settings(pygame, screen, self))
        self.screens.insert(2, HighScore(pygame, screen, self))

    def get_current_screen(self):
        return self.screens[self.screen_id]

    def change_screen(self, screen_id):
        self.screen_id = screen_id

