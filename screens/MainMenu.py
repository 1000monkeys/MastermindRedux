from array import array
import sys
from unittest.mock import call
from helpers.TextDisplay import TextDisplay
from helpers.Button import Button
import pygame

from helpers.Screen import Screen
from helpers.Button import Button
from screens.Settings import Settings

class MainMenu(Screen):
    def exit_button(self):
        sys.exit()

    def temp_play_button(self):
        self.display_manager.change_screen(Settings)

    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager

        self.background_image = pygame.transform.scale(
            pygame.image.load("assets/enigma.jpg"),
            (1024, 786)
        )

        self.texts = dict()
        self.texts["header_text"] = TextDisplay(
            screen,
            text="Welcome to Mastermind, Challenge your brain!",
            position=(10, 10),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=48
        )

        self.buttons = dict()
        self.buttons["play"] = Button(
            screen,
            text="Play",
            position=(50, 150),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            callback_function=self.temp_play_button
        )

        self.buttons["settings"] = Button(
            screen,
            text="Settings",
            position=(50, 250),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36
        )

        self.buttons["highscore"] = Button(
            screen,
            text="Highscore",
            position=(50, 350),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36
        )

        self.buttons["exit"] = Button(
            screen,
            text="Exit",
            position=(925, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            callback_function=self.exit_button
        )

    def draw(self):
        self.screen.blit(self.background_image, [0,0])

        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

        
    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].check_events(events)

        # for event in events:

