import pygame
from helpers.Button import Button
from helpers.MessageBox import MessageBox

from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum

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
        self.messageBox = None

    def exit_button(self):
        # Display text
        self.messageBox = MessageBox(
            self.screen,
            "Are you sure you want to quit the game?",
            "Yes",
            "No"
        )
        # self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.screen.blit(self.game_background_image, [1024 / 2 - 600 / 2, 786 / 2 - 600 / 2])

        for key in self.buttons.keys():
            self.buttons[key].draw()

        if self.messageBox is not None:
            self.messageBox.draw()


    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
