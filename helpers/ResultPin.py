import pygame


class ResultPin:
    def __init__(self, screen, assets, position) -> None:
        self.screen = screen
        self.assets = assets
        self.position = position

        self.image = self.assets.empty_pin

        self.position = (32 * position[0] + 300, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)

    def set_black(self):
        self.image = self.assets.black_pin

    def set_white(self):
        self.image = self.assets.white_pin

    def draw(self):
        self.screen.blit(self.image, self.rect)
