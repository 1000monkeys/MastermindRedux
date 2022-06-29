import pygame


class ResultPin:
    def __init__(self, screen, assets, position) -> None:
        self.screen = screen
        self.assets = assets
        self.position = position

        self.color = self.assets.gray

        self.position = (32 * position[0] + 300, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)
        self.border_rect = pygame.Rect(self.position[0] - 1, self.position[1] - 1, 26, 26)

    def set_black(self):
        self.color = self.assets.black

    def set_white(self):
        self.color = self.assets.white

    def draw(self):
        pygame.draw.rect(self.screen, self.assets.black, self.border_rect)        
        pygame.draw.rect(self.screen, self.color, self.rect)

