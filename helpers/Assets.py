import os
from platform import release
import sys
import pygame

class Assets:
    """This class contains all the assets used in the gamescreen and the background used in other screens.
    """
    def __init__(self) -> None:
        """Sets up the assets
        """
        self.release = True
        if self.release:
            self.main_background_image = pygame.image.load(self.resource_path("assets/enigma.jpg"))
            self.game_background_image = pygame.image.load(self.resource_path("assets/board.jpg"))
        else:
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
        if self.release:
            self.arrows = pygame.image.load(self.resource_path("assets/arrows.jpg"))
        else:
            self.arrows = pygame.image.load("assets/arrows.jpg")
        self.arrows = pygame.transform.scale(self.arrows, (64, 64))

        self.black = "#000000"
        self.white = "#FFFFFF"
        self.gray = "#808080"

        self.brown = (55, 42, 34)

    def resource_path(self, relative_path: str):
        """Used for release binary to get the included assets/images from the exe

        :param relative_path: The path of the item you want
        :type relative_path: str
        :return: The path
        :rtype: Path
        """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

