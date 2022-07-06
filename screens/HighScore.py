from __future__ import annotations
from typing import TYPE_CHECKING

from helpers.StaticFunctions import StaticFunctions

if TYPE_CHECKING:
    from helpers.DisplayManager import DisplayManager
    from helpers.Localisation import Localisation
    from helpers.Assets import Assets

import collections
import json
from operator import itemgetter
from os import path

import pygame
from helpers.Assets import Assets
from helpers.UIElements.Button import Button
from helpers.UIElements.HighScoreListing import HighScoreListing
from helpers.Localisation import Localisation
from helpers.Screen import Screen
from helpers.Enums.ScreenEnum import ScreenEnum
from helpers.Enums.SettingsEnum import SettingsEnum
from helpers.UIElements.TextDisplay import TextDisplay


class HighScore(Screen):
    def __init__(self, display_manager: DisplayManager, screen: Screen, localisation: Localisation, assets: Assets) -> None:
        super().__init__()
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.page = 0
        self.amount_per_page = 6

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )

        self.texts = dict()
        self.texts["header"] = TextDisplay(
            screen,
            text="Normal difficulty",
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

        self.buttons = dict()
        self.buttons["previous"] = Button(
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
        self.buttons["previous"].set_center_position((170, 600))

        self.buttons["easy"] = Button(
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
        self.buttons["easy"].set_center_position((340, 600))

        self.buttons["normal"] = Button(
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
        self.buttons["normal"].set_center_position((510, 600))

        self.buttons["difficult"] = Button(
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
        self.buttons["difficult"].set_center_position((680, 600))

        self.buttons["next"] = Button(
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
        self.buttons["next"].set_center_position((850, 600))

        self.difficulty = SettingsEnum.Difficulty.value.NORMAL.value
        self.populate_list()
        
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

    def easy(self) -> None:
        self.page = 0
        self.difficulty = SettingsEnum.Difficulty.value.EASY.value
        self.populate_list()
        self.texts["header"] = TextDisplay(
            self.screen,
            text="Easy difficulty",
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

    def normal(self) -> None:
        self.page = 0
        self.difficulty = SettingsEnum.Difficulty.value.NORMAL.value
        self.populate_list()
        self.texts["header"] = TextDisplay(
            self.screen,
            text="Normal difficulty",
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

    def difficult(self) -> None:
        self.page = 0
        self.difficulty = SettingsEnum.Difficulty.value.HARD.value
        self.populate_list()
        self.texts["header"] = TextDisplay(
            self.screen,
            text="Difficult difficulty",
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

    def populate_list(self) -> None:
        data = StaticFunctions.decrypt()
        if len(data[str(self.difficulty)]) > 0:
                scores = data[str(self.difficulty)]

                index = 0
                self.listings = dict()
                for name, score in scores.items():
                    position = (71, 81 + ((index % self.amount_per_page) * 75))

                    self.listings[index] = HighScoreListing(
                        screen=self.screen,
                        left_text=str(index + 1) + ": " + str(name),
                        right_text=str(score),
                        text_color=(255, 255, 255),
                        background_color=(0, 0, 0),
                        border_color=(255, 255, 255),
                        border_size=5,
                        position=position
                    )
                    index = index + 1
        else:
            self.no_listings = TextDisplay(
                screen=self.screen,
                text=self.localisation.current_language["no_scores"],
                position=(0, 0),
                text_color=(255, 255, 255),
                background_color=(55, 42, 34),
                border_color=(255, 255, 255),
                border_size=5,
                padding=4
            )
            self.no_listings.set_center_position((1024/2, 786/2))
            self.listings = dict()

    def next_page(self) -> None:
        self.page = self.page + 1
        if self.page > len(self.listings) / self.amount_per_page:
            self.page = self.page - 1

    def previous_page(self) -> None:
        self.page = self.page - 1
        if self.page < 0:
            self.page = 0

    def exit_button(self) -> None:
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def draw(self) -> None:
        super().draw()

        self.screen.blit(self.background_image, [0,0])

        for index in range(self.page * self.amount_per_page, (self.page + 1) * self.amount_per_page):
            if index < len(self.listings) and len(self.listings) > 0:
                self.listings[index].draw()
            elif len(self.listings) < 1:
                self.no_listings.draw()
        
        for key in self.buttons.keys():
            self.buttons[key].draw()

        for key in self.texts.keys():
            self.texts[key].draw()

    def handle_events(self, events: pygame.EventList) -> None:
        super().handle_events(events)

        for index in range(self.page * self.amount_per_page, (self.page + 1) * self.amount_per_page):
            if index < len(self.listings) and len(self.listings) > 0:
                self.listings[index].handle_events(events)
            elif len(self.listings) < 1:
                self.no_listings.handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

        for key in self.texts.keys():
            self.texts[key].handle_events(events)

                
