from cgitb import text
from itertools import repeat
import json
from os import path
from turtle import back
from typing import Text

import pygame
from helpers.Button import Button
from helpers.Container import Container
from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum
from helpers.SettingsEnum import SettingsEnum
from helpers.StaticFunctions import StaticFunctions
from helpers.TextDisplay import TextDisplay
from helpers.TextLoop import TextLoop

class Settings(Screen):
    def __init__(self, display_manager, screen, localisation, assets, setting_screen_positions) -> None:
        super().__init__()
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.setting_screen_positions = setting_screen_positions
        
        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )

        self.texts = dict()
        self.text_loops = dict()

        self.texts["option_menu"] = TextDisplay(
            screen,
            text=self.localisation.current_language["option_menu"],
            position=(50, 50),
            text_color=(255, 255, 255),
            font_size=48
        )

        self.texts["description"] = TextDisplay(
            screen,
            text=self.localisation.current_language["description"],
            position=(65, 125),
            text_color=(255, 255, 255),
            font_size=36
        )

        self.texts["language"] = TextDisplay(
            screen,
            text=self.localisation.current_language["language"],
            position=(90, 175),
            font_size=36
        )
        self.text_loops["language_loop"] = TextLoop(
            screen,
            texts=self.localisation.current_language["language_loop"],
            position=(800, 175),
            font_size=36,
            callback_function=self.change_language
        )

        self.texts["amount_game_rounds"] = TextDisplay(
            screen,
            text=self.localisation.current_language["amount_game_rounds"],
            position=(90, 225),
            font_size=36
        )       
        self.text_loops["amount_game_rounds_loop"] = TextLoop(
            screen,
            texts=self.localisation.current_language["amount_game_rounds_loop"],
            position=(800, 225),
            font_size=36,
            callback_function=self.update_difficulty
        )
        
        self.texts["time_guess"] = TextDisplay(
            screen,
            text=self.localisation.current_language["time_guess"],
            position=(90, 275),
            font_size=36
        )
        self.text_loops["time_guess_loop"] = TextLoop(
            screen,
            texts=self.localisation.current_language["time_guess_loop"],
            position=(800, 275),
            font_size=36,
            callback_function=self.update_difficulty
        )

        self.texts["repeating_colors"] = TextDisplay(
            screen,
            text=self.localisation.current_language["repeating_colors"],
            position=(90, 325),
            font_size=36
        )
        self.text_loops["repeating_colors_loop"] = TextLoop(
            screen,
            texts=self.localisation.current_language["repeating_colors_loop"],
            position=(800, 325),
            font_size=36,
            callback_function=self.update_difficulty
        )


        self.texts["empty_pins"] = TextDisplay(
            screen,
            text=self.localisation.current_language["empty_pins"],
            position=(90, 375),
            font_size=36
        )
        self.text_loops["empty_pins_loop"] = TextLoop(
            screen,
            texts=self.localisation.current_language["empty_pins_loop"],
            position=(800, 375),
            font_size=36,
            callback_function=self.update_difficulty
        )

        self.texts["difficulty"] = TextDisplay(
            screen,
            text=self.localisation.current_language["difficulty"],
            position=(65, 475),
            font_size=36
        )
        self.inner_buttons = dict()
        self.inner_buttons["easy_difficulty"] = Button(
            screen,
            text=self.localisation.moeilijkheid[SettingsEnum.Difficulty.value.EASY.value],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            border_size=5,
            padding=5,
            font_size=36,
            callback_function=self.easy
        )
        self.inner_buttons["easy_difficulty"].set_center_position((256, 575))
        self.inner_buttons["normal_difficulty"] = Button(
            screen,
            text=self.localisation.moeilijkheid[SettingsEnum.Difficulty.value.NORMAL.value],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            border_size=5,
            padding=5,
            font_size=36,
            callback_function=self.medium
        )
        self.inner_buttons["normal_difficulty"].set_center_position((512, 575))
        self.inner_buttons["hard_difficulty"] = Button(
            screen,
            text=self.localisation.moeilijkheid[SettingsEnum.Difficulty.value.HARD.value],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(0, 0, 0),
            border_size=5,
            padding=5,
            font_size=36,
            callback_function=self.hard
        )
        self.inner_buttons["hard_difficulty"].set_center_position((768, 575))

        self.texts["score_list_info"] = TextDisplay(
            screen,
            text=self.localisation.current_language["score_list_info"][0],
            position=(180, 625),
            font_size=36
        )

                                                    #   0           1               2
        self.merged_items = StaticFunctions.merge_dict(self.texts, self.text_loops, self.inner_buttons)
        self.container = Container(
            screen,
            self.merged_items,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=10
        )

        self.buttons = dict()
        self.buttons["back"] = Button(
            screen,
            text=self.localisation.current_language["save_and_exit"],
            position=(750, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_size=5,
            padding=5,
            font_size=36,
            callback_function=self.back
        )

        self.set_settings(self.setting_screen_positions)
        self.update_difficulty()

    def get_settings(self):
        language_pos = self.text_loops["language_loop"].get_option()
        game_rounds_pos = self.text_loops["amount_game_rounds_loop"].get_option()
        time_guess_pos = self.text_loops["time_guess_loop"].get_option()
        repeating_colors_pos = self.text_loops["repeating_colors_loop"].get_option()
        empty_pin_pos = self.text_loops["empty_pins_loop"].get_option()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": game_rounds_pos,
            "time_guess_pos": time_guess_pos,
            "repeating_colors_pos": repeating_colors_pos,
            "empty_pin_pos": empty_pin_pos
        }

        return positions

    def get_difficulty(self):
        game_rounds_pos = self.text_loops["amount_game_rounds_loop"].get_option()
        time_guess_pos = self.text_loops["time_guess_loop"].get_option()
        repeating_colors_pos = self.text_loops["repeating_colors_loop"].get_option()
        empty_pin_pos = self.text_loops["empty_pins_loop"].get_option()
 
        if game_rounds_pos == SettingsEnum.AmountGameRounds.value.ONE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.NONE.value and \
            repeating_colors_pos == SettingsEnum.RepeatingColors.value.NO.value and \
            empty_pin_pos == SettingsEnum.EmptyPins.value.NO.value:
                return 1
        elif game_rounds_pos == SettingsEnum.AmountGameRounds.value.THREE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.SIXTY.value and \
            repeating_colors_pos == SettingsEnum.RepeatingColors.value.YES.value and \
            empty_pin_pos == SettingsEnum.EmptyPins.value.NO.value:
                return 2
        elif game_rounds_pos == SettingsEnum.AmountGameRounds.value.FIVE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.THIRTY.value and \
            repeating_colors_pos == SettingsEnum.RepeatingColors.value.YES.value and \
            empty_pin_pos == SettingsEnum.EmptyPins.value.YES.value:
                return 3
        else:
            return 0

    def update_difficulty(self):
        # prelead by a number on how many of the dicts it is in merged items function call
        self.container.items["0-score_list_info"] = TextDisplay(
            self.screen,
            text=self.localisation.current_language["score_list_info"][self.get_difficulty()],
            position=(180, 625),
            font_size=36
        )

    def easy(self):
        language_pos = self.text_loops["language_loop"].get_option()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.ONE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.NONE.value,
            "repeating_colors_pos": SettingsEnum.RepeatingColors.value.NO.value,
            "empty_pin_pos": SettingsEnum.EmptyPins.value.NO.value
        }
        self.set_settings(positions)

    def medium(self):
        language_pos = self.text_loops["language_loop"].get_option()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.THREE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.SIXTY.value,
            "repeating_colors_pos": SettingsEnum.RepeatingColors.value.YES.value,
            "empty_pin_pos": SettingsEnum.EmptyPins.value.NO.value
        }
        self.set_settings(positions)

    def hard(self):
        language_pos = self.text_loops["language_loop"].get_option()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.FIVE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.THIRTY.value,
            "repeating_colors_pos": SettingsEnum.RepeatingColors.value.YES.value,
            "empty_pin_pos": SettingsEnum.EmptyPins.value.YES.value
        }
        self.set_settings(positions)

    def set_settings(self, setting_screen_positions):
        self.text_loops["language_loop"].set_option(setting_screen_positions["language_pos"])
        self.text_loops["amount_game_rounds_loop"].set_option(setting_screen_positions["game_rounds_pos"])
        self.text_loops["time_guess_loop"].set_option(setting_screen_positions["time_guess_pos"])
        self.text_loops["repeating_colors_loop"].set_option(setting_screen_positions["repeating_colors_pos"])
        self.text_loops["empty_pins_loop"].set_option(setting_screen_positions["empty_pin_pos"])
        self.update_difficulty()

    def save_settings(self):
        with open('settings.json', 'w') as f:
            f.write(json.dumps(self.get_settings()))

    def back(self):
        self.save_settings()
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def change_language(self):
        language_pos = self.text_loops["language_loop"].get_option()

        if language_pos >= len(self.localisation.languages):
            language_pos = 0

        self.localisation.set_language(language_pos)

        # Has to be last! Reinits the screens so code after does not get run!!
        self.save_settings()
        self.display_id = self.display_manager.get_current_screen_id()
        self.display_manager.__init__(self.screen, self.get_settings(), self.localisation, start_display_id=self.display_id)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.container.draw()

        """
        for key in self.texts.keys():
            self.texts[key].draw()
        """

        for key in self.text_loops.keys():
            self.text_loops[key].draw()

        for key in self.inner_buttons.keys():
            self.inner_buttons[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()
        
    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

        for key in self.inner_buttons.keys():
            self.inner_buttons[key].handle_events(events)

        for key in self.text_loops.keys():
            self.text_loops[key].handle_events(events)
        # for event in events:
