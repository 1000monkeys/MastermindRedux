import pygame
from helpers.Button import Button

from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum
from screens.MessageScreen import MessageScreen

class GameScreen(Screen):
    def __init__(self, display_manager, screen, localisation, assets, setting_screen_positions) -> None:
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.setting_screen_positions = setting_screen_positions

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )
        self.game_background_image = pygame.transform.scale(
            self.assets.game_background_image,
            (600, 600)
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

    def exit_button(self):
        messageScreen = MessageScreen(
            self.display_manager,
            self.screen,
            self.localisation,
            self.assets,
            "Are you sure you want to quit?",
            "Yes",
            self.exit_screen,
            "No",
            self.stay_in_game
        )
        self.display_manager.set_message_screen(messageScreen)


    def exit_screen(self):
        self.display_manager.set_message_screen(None)
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def stay_in_game(self):
        self.display_manager.set_message_screen(None)


    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.screen.blit(self.game_background_image, [1024 / 2 - 600 / 2, 786 / 2 - 600 / 2])

        for key in self.buttons.keys():
            self.buttons[key].draw()


    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
