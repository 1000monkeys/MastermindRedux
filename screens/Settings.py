from __future__ import annotations
from typing import TYPE_CHECKING

from screens.MessageScreen import MessageScreen

if TYPE_CHECKING:
    from helpers.DisplayManager import DisplayManager
    from helpers.Localisation import Localisation
    from helpers.Assets import Assets

import pygame
from helpers.UIElements.Button import Button
from helpers.UIElements.Container import Container
from helpers.Screen import Screen
from helpers.Enums.ScreenEnum import ScreenEnum
from helpers.Enums.SettingsEnum import SettingsEnum
from helpers.StaticFunctions import StaticFunctions
from helpers.UIElements.TextDisplay import TextDisplay
from helpers.UIElements.TextInput import TextInput
from helpers.UIElements.TextLoop import TextLoop

class Settings(Screen):
    def __init__(self, display_manager: DisplayManager, screen: Screen, localisation: Localisation, assets: Assets, setting_screen_positions: dict) -> None:
        """Initializes settings screen with all the needed ui elements and sets them to current setting

        :param display_manager: displaymanager used to change screen
        :type display_manager: DisplayManager
        :param screen: screen to draw to
        :type screen: Screen
        :param localisation: localisation file containing all strings
        :type localisation: Localisation
        :param assets: assets file containing all assets
        :type assets: Assets
        :param setting_screen_positions: current settings dictionary
        :type setting_screen_positions: dict
        """
        super().__init__()
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.setting_screen_positions = setting_screen_positions
        
        self.font_size = 36

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )

        self.texts = dict()
        self.texts["option_menu"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["option_menu"],
            position=(50, 45),
            text_color=self.assets.white,
            font_size=48
        )

        self.texts["description"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["description"],
            position=(65, 105),
            text_color=self.assets.white,
            font_size=self.font_size
        )

        self.texts["language"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["language"],
            position=(90, 150),
            font_size=self.font_size
        )

        self.text_loops = dict()
        self.text_loops["language_loop"] = TextLoop(
            screen,
            assets=self.assets,
            texts=self.localisation.current_language["language_loop"],
            position=(750, 150),
            font_size=self.font_size,
            callback_function=self.change_language
        )

        self.texts["amount_game_rounds"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["amount_game_rounds"],
            position=(90, 190),
            font_size=self.font_size
        )       
        self.text_loops["amount_game_rounds_loop"] = TextLoop(
            screen,
            assets=self.assets,
            texts=self.localisation.current_language["amount_game_rounds_loop"],
            position=(750, 190),
            font_size=self.font_size,
            callback_function=self.update_difficulty
        )
        
        self.texts["time_guess"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["time_guess"],
            position=(90, 230),
            font_size=self.font_size
        )
        self.text_loops["time_guess_loop"] = TextLoop(
            screen,
            assets=self.assets,
            texts=self.localisation.current_language["time_guess_loop"],
            position=(750, 230),
            font_size=self.font_size,
            callback_function=self.update_difficulty
        )


        self.texts["amount_pins"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["amount_pins"],
            position=(90, 270),
            font_size=self.font_size
        )
        self.text_loops["amount_pins_loop"] = TextLoop(
            screen,
            assets=self.assets,
            texts=self.localisation.current_language["amount_pins_loop"],
            position=(750, 270),
            font_size=self.font_size,
            callback_function=self.update_difficulty
        )

        self.texts["difficulty"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["difficulty"],
            position=(65, 315),
            font_size=self.font_size
        )
        self.inner_buttons = dict()
        self.inner_buttons["easy_difficulty"] = Button(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["difficulty_loop"][SettingsEnum.Difficulty.value.EASY.value],
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_size=5,
            padding=5,
            font_size=24,
            callback_function=self.easy
        )
        self.inner_buttons["easy_difficulty"].set_center_position((256, 400))
        self.inner_buttons["normal_difficulty"] = Button(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["difficulty_loop"][SettingsEnum.Difficulty.value.NORMAL.value],
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_size=5,
            padding=5,
            font_size=24,
            callback_function=self.medium
        )
        self.inner_buttons["normal_difficulty"].set_center_position((512, 400))
        self.inner_buttons["hard_difficulty"] = Button(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["difficulty_loop"][SettingsEnum.Difficulty.value.HARD.value],
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_size=5,
            padding=5,
            font_size=24,
            callback_function=self.hard
        )
        self.inner_buttons["hard_difficulty"].set_center_position((768, 400))

        self.texts["score_list_info"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["score_list_info"][0],
            position=(120, 430), # Also change in update_difficulty function
            font_size=self.font_size
        )

        self.texts["name"] = TextDisplay(
            screen,
            assets=self.assets,
            text="Name:",
            position=(120, 485),
            font_size=48
        )

        self.inputs = dict()
        self.inputs["name"] = TextInput(
            self.screen,
            assets=self.assets,
            text="",
            position=(240, 485),
            text_color=self.assets.white,
            background_color=self.assets.black,
            border_color=self.assets.white,
            border_width=3,
            max=10
        )

        self.texts["name_info"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["name_info"],
            position=(120, 550),
            font_size=32
        )
        self.texts["name_info_2"] = TextDisplay(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["name_info_2"],
            position=(120, 580),
            font_size=32
        )

                                                    #   0           1               2                   4
        self.merged_items = StaticFunctions.merge_dict(self.texts, self.text_loops, self.inner_buttons, self.inputs)
        self.container = Container(
            screen,
            assets=self.assets,
            items=self.merged_items,
            background_color=self.assets.brown,
            border_color=self.assets.white,
            border_size=10,
            padding=10
        )

        self.buttons = dict()
        self.buttons["back"] = Button(
            screen,
            assets=self.assets,
            text=self.localisation.current_language["save_and_exit"],
            position=(750, 700),
            text_color=self.assets.white,
            background_color=self.assets.brown,
            border_size=5,
            padding=5,
            font_size=36,
            callback_function=self.back
        )

        self.set_settings(self.setting_screen_positions)
        self.update_difficulty()

    def get_settings(self):
        """Returns current settings

        :return: current settings as dict
        :rtype: Dict
        """
        language_pos = self.text_loops["language_loop"].get_option()
        game_rounds_pos = self.text_loops["amount_game_rounds_loop"].get_option()
        time_guess_pos = self.text_loops["time_guess_loop"].get_option()
        amount_pins_pos = self.text_loops["amount_pins_loop"].get_option()
        name = self.inputs["name"].get_input()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": game_rounds_pos,
            "time_guess_pos": time_guess_pos,
            "amount_pins_pos": amount_pins_pos,
            "name": name
        }

        return positions

    def get_difficulty(self):
        """gets whether it is easy, normal, difficult or not a difficulty

        :return: integer signalling whether is is one of three difficulties or none of them
        :rtype: int
        """
        game_rounds_pos = self.text_loops["amount_game_rounds_loop"].get_option()
        time_guess_pos = self.text_loops["time_guess_loop"].get_option()
        amount_pins_pos = self.text_loops["amount_pins_loop"].get_option()
 
        if game_rounds_pos == SettingsEnum.AmountGameRounds.value.ONE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.NONE.value and \
            amount_pins_pos == SettingsEnum.AmountPins.value.FOUR.value:
                return 0
        elif game_rounds_pos == SettingsEnum.AmountGameRounds.value.THREE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.SIXTY.value and \
            amount_pins_pos == SettingsEnum.AmountPins.value.FIVE.value:
                return 1
        elif game_rounds_pos == SettingsEnum.AmountGameRounds.value.FIVE.value and \
            time_guess_pos == SettingsEnum.TimeGuess.value.THIRTY.value and \
            amount_pins_pos == SettingsEnum.AmountPins.value.SIX.value:
                return 2
        else:
            return -1

    def update_difficulty(self):
        """Updates the difficult high score info text display
        """
        # prelead by a number on how many of the dicts it is in merged items function call
        self.container.items["0-score_list_info"] = TextDisplay(
            self.screen,
            assets=self.assets,
            text=self.localisation.current_language["score_list_info"][self.get_difficulty()],
            position=(120, 430),
            font_size=36
        )

    def easy(self):
        """Changes settings to those of easy difficulty
        """
        language_pos = self.text_loops["language_loop"].get_option()
        name = self.inputs["name"].get_input()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.ONE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.NONE.value,
            "amount_pins_pos": SettingsEnum.AmountPins.value.FOUR.value,
            "name": name
        }
        self.set_settings(positions)

    def medium(self):
        """Changes settings to those of medium difficulty
        """
        language_pos = self.text_loops["language_loop"].get_option()
        name = self.inputs["name"].get_input()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.THREE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.SIXTY.value,
            "amount_pins_pos": SettingsEnum.AmountPins.value.FIVE.value,
            "name": name
        }
        self.set_settings(positions)

    def hard(self):
        """Changes settings to those of hard difficulty
        """
        language_pos = self.text_loops["language_loop"].get_option()
        name = self.inputs["name"].get_input()

        positions = {
            "language_pos": language_pos,
            "game_rounds_pos": SettingsEnum.AmountGameRounds.value.FIVE.value,
            "time_guess_pos": SettingsEnum.TimeGuess.value.THIRTY.value,
            "amount_pins_pos": SettingsEnum.AmountPins.value.SIX.value,
            "name": name
        }
        self.set_settings(positions)

    def set_settings(self, setting_screen_positions: dict):
        """Sets the inputs to the passed settings

        :param setting_screen_positions: Settings to set the inputs to
        :type setting_screen_positions: dict
        """
        self.text_loops["language_loop"].set_option(setting_screen_positions["language_pos"])
        self.text_loops["amount_game_rounds_loop"].set_option(setting_screen_positions["game_rounds_pos"])
        self.text_loops["time_guess_loop"].set_option(setting_screen_positions["time_guess_pos"])
        self.text_loops["amount_pins_loop"].set_option(setting_screen_positions["amount_pins_pos"])
        self.inputs["name"].set_input(setting_screen_positions["name"])
        self.update_difficulty()

    def save_settings(self):
        """Saves current settings
        """
        data = StaticFunctions.decrypt()
        data["settings"] = self.get_settings()
        StaticFunctions.encrypt(data)

    def back(self):
        """Leaves setting screen
        """
        if len(self.inputs["name"].get_input()) > 0:
            self.save_settings()
            self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)
        else:
            message_screen = MessageScreen(
                display_manager=self.display_manager,
                screen=self.screen,
                localisation=self.localisation,
                assets=self.assets,
                prompt_text=self.localisation.current_language["short_name"],
                right_option_text=self.localisation.current_language["okay"],
                right_option_callback=self.okay
            )
            self.display_manager.set_message_screen(message_screen)

    def okay(self):
        """Removes messages screen
        """
        self.display_manager.set_message_screen(None)

    def change_language(self):
        """Changes language to the option in language_pos
        """
        language_pos = self.text_loops["language_loop"].get_option()

        if language_pos >= len(self.localisation.languages):
            language_pos = 0

        self.localisation.set_language(language_pos)

        # Has to be last! Reinits the screens so code after does not get run!!
        self.save_settings()
        self.display_id = self.display_manager.get_current_screen_id()
        self.display_manager.__init__(self.screen, self.get_settings(), self.localisation, start_display_id=self.display_id)

    def draw(self):
        """Draw method which draws all ui elements
        """
        super().draw()

        self.screen.blit(self.background_image, [0,0])
        
        self.container.draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()
        
    def handle_events(self, events):
        """Handles events passed here from the screen

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)

        self.container.handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
