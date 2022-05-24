import pygame

from helpers.DisplayManager import DisplayManager

class Game():
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 786))
        pygame.display.set_caption("Mastermind")
        self.display_manager = DisplayManager(self.screen)

    def run_loop(self):
        ms_per_frame = 1000/60
        last_frame_ms = 0
        while True:
            pygame.time.Clock().tick(30)
            current_display = self.display_manager.get_current_screen()
            events = pygame.event.get()
            current_display.handle_events(events)
            current_display.draw()
            pygame.display.flip()

game = Game()
game.run_loop()
