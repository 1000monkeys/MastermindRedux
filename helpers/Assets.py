import pygame


class Assets:
    def __init__(self) -> None:
        self.main_background_image = pygame.image.load("assets/enigma.jpg")
        self.game_background_image = pygame.image.load("assets/board.jpg")

        self.color_pins = [
            "#ffe119", #yellow
            "#e6194B", #red
            "#3cb44b", #green
            "#911eb4", #purple
            "#f58231", #orange
            "#000075", #navy
            "#42d4f4", #cyan
            "#f032e6" #magenta
        ]

        self.arrows = pygame.image.load("assets/arrows.jpg")
        self.arrows = pygame.transform.scale(self.arrows, (64, 64))

        self.black = "#000000"
        self.white = "#FFFFFF"
        self.gray = "#808080"

