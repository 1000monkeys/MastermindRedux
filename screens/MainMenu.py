import sys
from unittest.mock import call
from helpers.Assets import Assets
from helpers.Localisation import Localisation
from helpers.TextDisplay import TextDisplay
from helpers.Button import Button
from helpers.Screen import Screen
from helpers.Button import Button
from screens.Settings import Settings

class MainMenu(Screen):
    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager
        self.localisation = Localisation()
        self.assets = Assets()

        self.background_image = pygame.transform.scale(
            self.assets.background_image,
            (1024, 786)
        )

        self.texts = dict()
        self.texts["welcome"] = TextDisplay(
            screen,
            text=self.localisation.current_language["welcome"],
            position=(25, 25),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=5,
            font_size=48,
            padding=5
        )

        self.buttons = dict()
        self.buttons["play"] = Button(
            screen,
            text=self.localisation.current_language["play"],
            position=(75, 150),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5
        )

        self.buttons["settings"] = Button(
            screen,
            text=self.localisation.current_language["settings"],
            position=(75, 250),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.setting_button
        )

        self.buttons["highscore"] = Button(
            screen,
            text=self.localisation.current_language["highscore"],
            position=(75, 350),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.highscore_button
        )

        self.buttons["exit"] = Button(
            screen,
            text=self.localisation.current_language["exit"],
            position=(850, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )

    def exit_button(self):
        sys.exit()

    def setting_button(self):
        self.display_manager.change_screen(1)

    def highscore_button(self):
        self.display_manager.change_screen(2)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])

        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

        
    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

        # for event in events:

