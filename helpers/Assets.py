import pygame


class Assets:
    def __init__(self) -> None:
        self.main_background_image = pygame.image.load("assets/enigma.jpg")
        self.game_background_image = pygame.image.load("assets/board.jpg")
