import pygame


class Assets:
    def __init__(self) -> None:
        self.main_background_image = pygame.image.load("assets/enigma.jpg")
        self.game_background_image = pygame.image.load("assets/board.jpg")

        self.color_pins = [
            pygame.image.load("assets/bluepin.bmp"),
            pygame.image.load("assets/greenpin.bmp"),
            pygame.image.load("assets/brownpin.bmp"),
            pygame.image.load("assets/redpin.bmp"),
            pygame.image.load("assets/greypin.bmp"),
            pygame.image.load("assets/yellowpin.bmp"),
            pygame.image.load("assets/maroonpin.bmp"),
            pygame.image.load("assets/purplepin.bmp")
        ]

        self.arrows = pygame.image.load("assets/arrows.jpg")
        self.arrows = pygame.transform.scale(self.arrows, (64, 64))

        self.black_pin = pygame.image.load("assets/blackpin.bmp")
        self.white_pin = pygame.image.load("assets/whitepin.bmp")
        self.empty_pin = pygame.image.load("assets/emptypin.bmp")

