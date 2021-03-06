from __future__ import annotations
from types import FunctionType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from helpers.DisplayManager import DisplayManager
    from helpers.Localisation import Localisation
    from helpers.Assets import Assets

from turtle import screensize
import pygame
from helpers.UIElements.Button import Button
from helpers.Screen import Screen
from helpers.UIElements.TextDisplay import TextDisplay


class MessageScreen(Screen):
    def __init__(self, display_manager: DisplayManager, screen: Screen, localisation: Localisation, assets: Assets, prompt_text: str, left_option_text: str=None, left_option_callback: FunctionType=None, right_option_text: str=None, right_option_callback: FunctionType=None) -> None:
        super().__init__()
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        
        self.prompt_text = prompt_text

        self.left_option_text = left_option_text
        self.left_option_callback = left_option_callback

        self.right_option_text = right_option_text
        self.right_option_callback = right_option_callback

        self.texts = dict()
        self.texts["prompt_text"] = TextDisplay(
            screen=screen,
            assets=self.assets,
            text=self.prompt_text,
            position=(0, 0),
            text_color=self.assets.white,
            background_color=self.assets.brown,
            border_color=self.assets.white,
            border_size=5,
            padding=25
        )
        self.texts["prompt_text"].set_center_position((1024/2, 786/2 - 200))

        self.buttons = dict()
        if self.left_option_text is not None and self.left_option_callback is not None:
            self.buttons["left_option"] = Button(
                screen,
                assets=self.assets,
                text=self.left_option_text,
                position=(256, 700),
                text_color=self.assets.white,
                background_color=self.assets.brown,
                font_size=36,
                border_size=5,
                padding=5,
                callback_function=self.left_option_callback
            )
            self.buttons["left_option"].set_center_position((256, 700))

        if self.right_option_text is not None and self.right_option_callback is not None:
            self.buttons["right_option"] = Button(
                screen,
                assets=self.assets,
                text=self.right_option_text,
                position=(768, 700),
                text_color=self.assets.white,
                background_color=self.assets.brown,
                font_size=36,
                border_size=5,
                padding=5,
                callback_function=self.right_option_callback
            )
            self.buttons["right_option"].set_center_position((768, 700))

        if self.left_option_text is None and \
                self.left_option_callback is None and \
                self.right_option_text is not None and \
                self.right_option_callback is not None:
            self.buttons["right_option"].set_center_position((512, 700))

        self.background = pygame.Surface((1024, 786))
        self.background.set_alpha(195)
        self.background.fill(self.assets.black)

    def draw(self):
        """Draw method which draws all ui elements
        """
        super().draw()

        self.screen.blit(self.background, (0, 0))

        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

    def handle_events(self, events):
        """Handles events passed here from the screen

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

