import collections
import json
from operator import itemgetter
from os import path
from turtle import update
import pygame

from helpers.DisplayManager import DisplayManager

class Game():
    def __init__(self) -> None:
        if path.exists("settings.json"):
            with open('settings.json') as f:
                setting_screen_positions = json.load(f)
        else:
            setting_screen_positions = {
                "language_pos": 0,
                "game_rounds_pos": 0,
                "time_guess_pos": 0,
                "amount_pins_pos": 0
            }

        pygame.init()

        self.screen = pygame.display.set_mode((1024, 786))
        pygame.display.set_caption("Mastermind")
        self.display_manager = DisplayManager(self.screen, setting_screen_positions)

    def run_loop(self):
        self.update_score()
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

    def update_score(self):
        scores = self.open_score()

        scores["1vvzzant"] = 99999
        with open(str(0) + 'high_scores.json', 'w') as f:
            f.write(json.dumps(scores))

    def open_score(self):
        if path.exists(str(0) + "high_scores.json"):
            with open(str(0) + 'high_scores.json') as f:
                scores = json.load(f)
                scores = collections.OrderedDict(scores)
                return scores
        else:
            return collections.OrderedDict()

game = Game()
game.run_loop()
