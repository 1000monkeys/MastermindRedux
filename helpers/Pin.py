import pygame


class Pin:
    def __init__(self, screen, assets, position) -> None:
        self.screen = screen
        self.assets = assets
        self.position = position
        self.changed = False

        self.color = 0

        self.position = (32 * position[0] + 68, 32 * position[1] + 150)
        self.rect = pygame.Rect(self.position[0], self.position[1], 24, 24)

    def next_color(self):
        if self.changed:
            if self.color + 1 == len(self.assets.color_pins):
                self.color = 0
            else:
                self.color = self.color + 1
        else:
            self.changed = True
            self.color = 0
        self.image = self.assets.color_pins[self.color]

    def draw(self):
        if self.changed:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.assets.empty_pin, self.rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.next_color()
