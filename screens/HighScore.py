import collections
import json
from operator import contains, itemgetter
from os import path
import sys

import pygame
from helpers.Assets import Assets
from helpers.Button import Button
from helpers.Container import Container
from helpers.HighScoreListing import HighScoreListing
from helpers.Localisation import Localisation
from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum
from helpers.SettingsEnum import SettingsEnum
from helpers.StaticFunctions import StaticFunctions
from helpers.TextDisplay import TextDisplay


class HighScore(Screen):
    def __init__(self, display_manager, screen, localisation, assets) -> None:
        super().__init__()
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )

        self.inner_buttons = dict()
        self.inner_buttons["previous"] = Button(
            screen,
            text="Previous",
            position=(170, 600),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.previous_page
        )
        self.inner_buttons["previous"].set_center_position((170, 600))

        self.inner_buttons["easy"] = Button(
            screen,
            text="Easy",
            position=(340, 600),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.easy
        )
        self.inner_buttons["easy"].set_center_position((340, 600))

        self.inner_buttons["normal"] = Button(
            screen,
            text="Normal",
            position=(510, 600),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.normal
        )
        self.inner_buttons["normal"].set_center_position((510, 600))

        self.inner_buttons["difficult"] = Button(
            screen,
            text="Difficult",
            position=(680, 600),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.difficult
        )
        self.inner_buttons["difficult"].set_center_position((680, 600))

        self.inner_buttons["next"] = Button(
            screen,
            text="Next",
            position=(950, 600),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.next_page
        )
        self.inner_buttons["next"].set_center_position((850, 600))

        self.difficulty = self.display_manager.screens[ScreenEnum.SETTINGS.value].get_difficulty()
        self.populate_list()
        
        self.merged_items = StaticFunctions.merge_dict(self.listings, self.inner_buttons)
        self.container = Container(
            screen,
            self.merged_items,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=25
        )

        self.buttons = dict()
        self.buttons["exit"] = Button(
            screen,
            text=self.localisation.current_language["back"],
            position=(850, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )

    def easy(self):
        self.difficulty = SettingsEnum.Difficulty.value.EASY.value
        self.populate_list()

    def normal(self):
        self.difficulty = SettingsEnum.Difficulty.value.NORMAL.value
        self.populate_list()

    def difficult(self):
        self.difficulty = SettingsEnum.Difficulty.value.HARD.value
        self.populate_list()

    def populate_list(self):
        print(self.difficulty)
        if path.exists(str(self.difficulty) + "high_scores.json"):
            with open(str(self.difficulty) + 'high_scores.json') as f:
                self.json_data = json.load(f)
                self.json_data = collections.OrderedDict(sorted(self.json_data.items(), key=itemgetter(1), reverse=True))

                index = 0
                self.listings = dict()
                for key, value in self.json_data.items():
                    self.listings[index] = HighScoreListing(
                        screen=self.screen,
                        left_text=str(index + 1) + ": " + str(key),
                        right_text=str(value),
                        text_color=(255, 255, 255),
                        background_color=(0, 0, 0),
                        border_color=(255, 255, 255),
                        border_size=5,
                        index=index
                    )
                    index = index + 1

                self.merged_items = StaticFunctions.merge_dict(self.listings, self.inner_buttons)
                self.container = Container(
                    self.screen,
                    self.merged_items,
                    background_color=(55, 42, 34),
                    border_color=(255, 255, 255),
                    border_size=10,
                    padding=25
                )
        else:
            self.listings = {
                "No scores!": TextDisplay(
                    screen=self.screen,
                    text=self.localisation.current_language["no_scores"],
                    position=(0, 0),
                    text_color=(255, 255, 255),
                )
            }
            self.listings["No scores!"].set_center_position((1024/2, 786/2))

    def next_page(self):
        pass

    def previous_page(self):
        pass

    def exit_button(self):
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])

        self.container.draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

    def handle_events(self, events):
        super().handle_events(events)

        self.container.handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
