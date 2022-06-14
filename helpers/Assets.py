import pygame


class Assets:
    def __init__(self) -> None:
        self.main_background_image = pygame.image.load("assets/enigma.jpg")
        self.game_background_image = pygame.image.load("assets/board.jpg")

        self.color_pins = [
            pygame.image.load("assets/bluepin.bmp").convert(),
            pygame.image.load("assets/greenpin.bmp").convert(),
            pygame.image.load("assets/brownpin.bmp").convert(),
            pygame.image.load("assets/redpin.bmp").convert(),
            pygame.image.load("assets/greypin.bmp").convert(),
            pygame.image.load("assets/yellowpin.bmp").convert()
        ]

        self.black_pin = pygame.image.load("assets/blackpin.bmp").convert()
        self.white_pin = pygame.image.load("assets/whitepin.bmp").convert()
        self.empty_pin = pygame.image.load("assets/emptypin.bmp").convert()

