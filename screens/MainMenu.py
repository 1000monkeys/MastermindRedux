import pygame

from helpers.Screen import Screen

class MainMenu(Screen):
    def __init__(self, pygame, screen) -> None:
        super().__init__()
        self.screen = screen
        self.pygame = pygame
        self.background_image = pygame.transform.scale(
            pygame.image.load("C:/Users/kjell/OneDrive/Afbeeldingen/datagame.png").convert(),
            [1024, 786]
        )

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.background_image, [1024, 768]), [0,0])

    def handle_events(self, events):
        return super().handle_events(events)
        for event in events:
            continue