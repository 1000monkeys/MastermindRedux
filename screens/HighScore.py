from __future__ import annotations
from typing import TYPE_CHECKING

from helpers.StaticFunctions import StaticFunctions

if TYPE_CHECKING:
    from helpers.DisplayManager import DisplayManager
    from helpers.Localisation import Localisation
    from helpers.Assets import Assets


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
        """Initializes the high score page with the needed data and ui elements

        :param display_manager: The display manager used for switching displays
        :type display_manager: DisplayManager
        :param screen: Screen to draw to
        :type screen: Screen
        :param localisation: Localisation containing all the strings
        :type localisation: Localisation
        :param assets: Assets containing all the needed files
        :type assets: Assets
        """
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
            assets=self.assets,
            text=self.localisation.current_language["difficulty_header"][1],
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.brown,
            border_color=self.assets.white,
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

        self.buttons = dict()
        self.buttons["previous"] = Button(
            screen,
            assets=self.assets,
            text="Previous",
            position=(170, 600),
            text_color=self.assets.white,
            background_color=self.assets.black,
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.previous_page
        )
        self.buttons["previous"].set_center_position((170, 600))

        self.buttons["easy"] = Button(
            screen,
            assets=self.assets,
            text="Easy",
            position=(340, 600),
            text_color=self.assets.white,
            background_color=self.assets.black,
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.easy
        )
        self.buttons["easy"].set_center_position((340, 600))

        self.buttons["normal"] = Button(
            screen,
            assets=self.assets,
            text="Normal",
            position=(510, 600),
            text_color=self.assets.white,
            background_color=self.assets.black,
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.normal
        )
        self.buttons["normal"].set_center_position((510, 600))

        self.buttons["difficult"] = Button(
            screen,
            assets=self.assets,
            text="Difficult",
            position=(680, 600),
            text_color=self.assets.white,
            background_color=self.assets.black,
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.difficult
        )
        self.buttons["difficult"].set_center_position((680, 600))

        self.buttons["next"] = Button(
            screen,
            assets=self.assets,
            text="Next",
            position=(950, 600),
            text_color=self.assets.white,
            background_color=self.assets.black,
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
            assets=self.assets,
            text=self.localisation.current_language["back"],
            position=(850, 700),
            text_color=self.assets.white,
            background_color=self.assets.brown,
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )

    def change_difficulty(self, difficulty: int) -> None:
        """Changes header and high score listings to the passed difficulty

        :param difficulty: The difficulty to change to
        :type difficulty: int
        """
        self.page = 0
        self.difficulty = difficulty
        self.populate_list()
        self.texts["header"] = TextDisplay(
            self.screen,
            assets=self.assets,
            text=self.localisation.current_language["difficulty_header"][self.difficulty],
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.brown,
            border_color=self.assets.white,
            font_size=36,
            border_size=5,
            padding=5
        )
        self.texts["header"].set_center_position((512, 35))

    def easy(self) -> None:
        """Changes difficulty to easy
        """
        self.change_difficulty(SettingsEnum.Difficulty.value.EASY.value)

    def normal(self) -> None:
        """Change difficulty to normal
        """
        self.change_difficulty(SettingsEnum.Difficulty.value.NORMAL.value)

    def difficult(self) -> None:
        """Changes difficulty to hard
        """
        self.change_difficulty(SettingsEnum.Difficulty.value.HARD.value)

    def populate_list(self) -> None:
        """Populates the high score listings or if there are no listings sets the info text
        """
        data = StaticFunctions.decrypt()
        if len(data[str(self.difficulty)]) > 0:
                scores = data[str(self.difficulty)]

                index = 0
                self.listings = dict()
                for name, score in scores.items():
                    position = (71, 81 + ((index % self.amount_per_page) * 75))

                    self.listings[index] = HighScoreListing(
                        screen=self.screen,
                        assets=self.assets,
                        left_text=str(index + 1) + ": " + str(name),
                        right_text=str(score),
                        text_color=self.assets.white,
                        background_color=self.assets.black,
                        border_color=self.assets.white,
                        border_size=5,
                        position=position
                    )
                    index = index + 1
        else:
            self.no_listings = TextDisplay(
                screen=self.screen,
                assets=self.assets,
                text=self.localisation.current_language["no_scores"],
                position=(0, 0),
                text_color=self.assets.white,
                background_color=self.assets.brown,
                border_color=self.assets.white,
                border_size=5,
                padding=4
            )
            self.no_listings.set_center_position((1024/2, 786/2))
            self.listings = dict()

    def next_page(self) -> None:
        """Goes to the next page if possible
        """
        self.page = self.page + 1
        if self.page > len(self.listings) / self.amount_per_page:
            self.page = self.page - 1

    def previous_page(self) -> None:
        """Goes to the previous page if possible
        """
        self.page = self.page - 1
        if self.page < 0:
            self.page = 0

    def exit_button(self) -> None:
        """Exits the high score page to the main menu
        """
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def draw(self) -> None:
        """Draw method which draws all ui elements
        """
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
        """Handles events passed here from the screen

        :param events: Events to check
        :type events: pygame.EventList
        """
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

                
