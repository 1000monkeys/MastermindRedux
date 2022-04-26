import pygame

class TextDisplay:
    def __init__(self, screen, text, position, text_color, background_color, font_size=36, padding=5) -> None:
        self.screen = screen
        self.text = text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.padding = padding
        self.font_size = font_size

        self.font = pygame.font.SysFont("arial", self.font_size)
        self.font_width, self.font_height = self.font.size(text)

        self.border_rect = pygame.Rect(
            self.position[0],
            self.position[1],
            self.font_width + self.padding * 4,
            self.font_height + self.padding * 4
        )

        self.rect = pygame.Rect(
            self.position[0] + padding,
            self.position[1] + padding,
            self.font_width + self.padding * 2,
            self.font_height + self.padding * 2
        )

        self.text_rendered = self.font.render(
            text,
            True,
            self.text_color,
            self.background_color
        )

        self.text_rect = self.text_rendered.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.text_color, self.border_rect)
        self.screen.fill(self.background_color, self.rect)
        self.screen.blit(self.text_rendered, self.text_rect)
        pass

    def check_events(self):
        pass