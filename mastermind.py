import collections
import json
from operator import itemgetter
from os import path
import os
from turtle import update
import pygame

from helpers.DisplayManager import DisplayManager
from helpers.Enums.ScreenEnum import ScreenEnum

class Game():
    """The main game class containing the startup sequence for the game
    Also contains the main game loop which runs with a while True
    """
    def __init__(self) -> None:
        if path.exists("data/settings.json"):
            with open('data/settings.json') as f:
                setting_screen_positions = json.load(f)
        else:
            setting_screen_positions = {
                "language_pos": 0,
                "game_rounds_pos": 0,
                "time_guess_pos": 0,
                "amount_pins_pos": 0,
                "name": "user"
            }

        pygame.init()

        self.screen = pygame.display.set_mode((1024, 786))
        pygame.display.set_caption("Mastermind")

        self.display_manager = DisplayManager(self.screen, setting_screen_positions)
        if not path.exists("data"):
            os.mkdir("data")
        if not path.exists("data/settings.json"):
            with open('data/settings.json', 'w') as f:
                f.write(json.dumps(setting_screen_positions))
        if not path.exists("data/0highscore.json"):
            with open('data/0high_scores.json', 'w') as f:
                f.write(json.dumps(dict()))
        if not path.exists("data/1highscore.json"):
            with open('data/1high_scores.json', 'w') as f:
                f.write(json.dumps(dict()))
        if not path.exists("data/2highscore.json"):
            with open('data/2high_scores.json', 'w') as f:
                f.write(json.dumps(dict()))
    
    def run_loop(self):
        while True:
            pygame.time.Clock().tick(30)
            current_display = self.display_manager.get_current_screen()
            events = pygame.event.get()
            if self.display_manager.message_screen is None:
                current_display.handle_events(events)
                current_display.draw()
            else:
                current_display.draw()
                self.display_manager.message_screen.draw()
                self.display_manager.message_screen.handle_events(events)
            pygame.display.flip()

game = Game()
game.run_loop()

# pyinstaller-script.py --noconsole --onefile .\mastermind.py --hidden-import pygame --add-binary "assets/arrows.jpg;assets" --add-binary "assets/enigma.jpg;assets" --add-binary "assets/board.jpg;assets"