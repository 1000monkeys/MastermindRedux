import sys
from turtle import back
from typing import Text
from helpers.Button import Button
from helpers.Container import Container
from helpers.Screen import Screen
from helpers.TextDisplay import TextDisplay

class Settings(Screen):
    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager

        self.background_image = pygame.transform.scale(
            pygame.image.load("assets/enigma.jpg"),
            (1024, 786)
        )

        items = list()
        items.append(
            TextDisplay(
                screen,
                text="Optie menu:",
                #text="Welcome to Mastermind, Challenge your brain!",
                position=(50, 50),
                text_color=(255, 255, 255),
                font_size=48
            )
        )
        items.append(
            TextDisplay(
                screen,
                text="Taal:",
                position=(65, 175),
                font_size=36
            )
        )

        self.container = Container(
            screen,
            items,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=10
        )

        self.buttons = dict()
        self.buttons["back"] = Button(
            screen,
            text="Back",
            position=(925, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            callback_function=self.back
        )

    def back(self):
        self.display_manager.change_screen(0)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.container.draw()
        """
        for key in self.texts.keys():
            self.texts[key].draw()
        """
        for key in self.buttons.keys():
            self.buttons[key].draw()
        
    def handle_events(self, events):
        super().handle_events(events)
        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
        # for event in events:
