from distutils.fancy_getopt import wrap_text
from turtle import position, width
import pygame

from helpers.UIElement import UIElement

class TextDisplay(UIElement):
    def __init__(self, screen, text, position, text_color=(255, 255, 255), background_color=None, border_color=None, border_size=0, font_size=36, padding=0, width=None) -> None:
        self.screen = screen
        self.text = text
        self.position = position
        self.text_color = text_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_size = border_size
        self.font_size = font_size
        self.padding = padding
        self.width = width

        self.font = pygame.font.SysFont("arial", self.font_size)
        if self.width is None:
            self.font_width, self.font_height = self.font.size(text)

            if border_color is not None:
                self.border_rect = pygame.Rect(
                    self.position[0] - self.padding - self.border_size,
                    self.position[1] - self.padding - self.border_size,
                    self.font_width + self.padding * 2 + self.border_size * 2,
                    self.font_height + self.padding * 2 + self.border_size * 2
                )
            else:
                self.border_rect = None

            self.rect = pygame.Rect(
                self.position[0] - self.padding,
                self.position[1] - self.padding,
                self.font_width + self.padding * 2,
                self.font_height + self.padding * 2
            )

            self.text_rendered = self.font.render(
                text,
                True,
                self.text_color,
                self.background_color,
            )
            self.text_rect = self.text_rendered.get_rect(center=(self.rect.center))
        else:
            self.lines = self.create_wrapped_text_list(self.text, self.font, self.width)
            self.surface = self.render_text_lists(self.lines)


            self.rect = pygame.Rect(
                self.position[0] - self.padding,
                self.position[1] - self.padding,
                self.width + self.padding * 2,
                len(self.lines) * self.font.get_linesize() + self.padding * 2
            )

            self.text_rect = self.surface.get_rect(center=(self.rect.center))

            if border_color is not None:
                self.border_rect = pygame.Rect(
                    self.position[0] - self.padding - self.border_size,
                    self.position[1] - self.padding - self.border_size,
                    self.width + (self.padding * 2) + (self.border_size * 2),
                    len(self.lines) * self.font.get_linesize()  + (self.padding * 2) + (self.border_size * 2)
                )

    def get_rect(self):
        return self.rect

    def create_wrapped_text_list(self, text, font, width):
        """Wrap text to fit inside a given width when rendered.
        :param text: The text to be wrapped.
        :param font: The font the text will be rendered in.
        :param width: The width to wrap to.
        """
        text_lines = text.replace('\t', '    ').split('\n')
        if width is None or width == 0:
            return text_lines

        wrapped_lines = []
        for line in text_lines:
            line = line.rstrip() + ' '
            if line == ' ':
                wrapped_lines.append(line)
                continue

            # Get the leftmost space ignoring leading whitespace
            start = len(line) - len(line.lstrip())
            start = line.index(' ', start)
            while start + 1 < len(line):
                # Get the next potential splitting point
                next = line.index(' ', start + 1)
                if font.size(line[:next])[0] <= width:
                    start = next
                else:
                    wrapped_lines.append(line[:start])
                    line = line[start+1:]
                    start = line.index(' ')
            line = line[:-1]
            if line:
                wrapped_lines.append(line)
        return wrapped_lines

    def render_text_lists(self, lines):
        rendered = [self.font.render(line, True, self.text_color).convert_alpha() for line in lines]

        line_height = self.font.get_linesize()
        width = max(line.get_width() for line in rendered)
        tops = [int(round(i * line_height)) for i in range(len(rendered))]
        height = tops[-1] + self.font.get_height()

        surface = pygame.Surface((width, height)).convert_alpha()
        surface.fill(self.background_color)
        for y, line in zip(tops, rendered):
            surface.blit(line, (0, y))
        return surface

    def set_center_position(self, position):
        if self.border_rect is not None:
            self.border_rect.center = position
        self.rect.center = position
        self.text_rect.center = position

    def draw(self):
        if self.width is None:
            if self.border_color is not None:
                self.screen.fill(self.border_color, self.border_rect)
            if self.background_color is not None:
                self.screen.fill(self.background_color, self.rect)
            self.screen.blit(self.text_rendered, self.text_rect)
        else:
            if self.border_color is not None:
                self.screen.fill(self.border_color, self.border_rect)
            if self.background_color is not None:
                self.screen.fill(self.background_color, self.rect)
            self.screen.blit(self.surface, self.text_rect)

    def handle_events(self, events):
        pass