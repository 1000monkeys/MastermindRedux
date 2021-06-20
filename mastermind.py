import pygame
from helpers.DisplayManager import DisplayManager

pygame.init()

screen = pygame.display.set_mode((1024, 786))
pygame.display.set_caption("Mastermind")
display_manager = DisplayManager(pygame, screen)

while True:
    current_display = display_manager.get_current_screen()
    events = pygame.event.get()
    current_display.handle_events(events)
    current_display.draw()
    pygame.display.flip()
