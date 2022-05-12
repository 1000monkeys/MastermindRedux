import collections
import json
from operator import contains, itemgetter
from os import path
import sys
from helpers.Button import Button
from helpers.Container import Container
from helpers.HighScoreListing import HighScoreListing
from helpers.Screen import Screen
from helpers.TextDisplay import TextDisplay


class HighScore(Screen):
    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager

        self.background_image = pygame.transform.scale(
            pygame.image.load("assets/enigma.jpg"),
            (1024, 786)
        )

        if path.exists("high_scores.json"):
            with open('high_scores.json') as f:
                self.json_data = json.load(f)
                self.json_data = collections.OrderedDict(sorted(self.json_data.items(), key=itemgetter(1), reverse=True))

                index = 1
                self.listings = dict()
                for key, value in self.json_data.items():
                    self.listings[index] = HighScoreListing(
                        screen=screen,
                        left_text=str(index) + ": " + str(key),
                        right_text=str(value[0]),
                        text_color=(255, 255, 255),
                        background_color=(0, 0, 0),
                        border_color=(255, 255, 255),
                        border_size=5
                    )
        else:
            self.listings = {
                "No scores!": TextDisplay(
                    screen=screen,
                    text="Er zijn nog geen high scores!",
                    position=(0, 0),
                    text_color=(255, 255, 255)
                )
            }
            self.listings["No scores!"].set_position((1024/2, 786/2))
        
        self.container = Container(
            screen,
            self.listings,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=10
        )

        self.buttons = dict()
        self.buttons["exit"] = Button(
            screen,
            text="Back",
            position=(925, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )

    def exit_button(self):
        self.display_manager.change_screen(0)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.container.draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)
