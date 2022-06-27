import collections
import json
from operator import itemgetter
from os import path
import pygame

from helpers.DisplayManager import DisplayManager

class Game():
    def __init__(self) -> None:
        if path.exists("settings.json"):
            with open('settings.json') as f:
                setting_screen_positions = json.load(f)
                setting_screen_positions = collections.OrderedDict(sorted(setting_screen_positions.items(), key=itemgetter(1), reverse=True))
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
