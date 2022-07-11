from __future__ import annotations

from ctypes import Array
from typing import Tuple
import pygame
from helpers.Assets import Assets
from helpers.Screen import Screen

from helpers.UIElement import UIElement

class TextDisplay(UIElement):
    def __init__(self, screen: Screen, assets: Assets, text: str, position: Tuple, text_color: Tuple=(255, 255, 255), background_color: Tuple=None, border_color: Tuple=None, border_size: int=0, font_size: int=36, padding: int=0, width: int=None) -> None:
        """_summary_

        :param screen: Screen to draw the result pin to
        :type screen: Screen
        :param text: Text to display
        :type text: str
        :param position: position to place the TextDisplay
        :type position: Tuple
        :param text_color: Color of the text, RGB value, defaults to (255, 255, 255)
        :type text_color: Tuple, optional
        :param background_color: Color behind the text, RGB value, defaults to None
        :type background_color: Tuple, optional
        :param border_color: border color around the background, defaults to None
        :type border_color: Tuple, optional
        :param border_size: size of the border in pixels, defaults to 0
        :type border_size: int, optional
        :param font_size: Size of the text/font, defaults to 36
        :type font_size: int, optional
        :param padding: padding inside, between text and border, defaults to 0
        :type padding: int, optional
        :param width: max width after which the text will be wrapped, defaults to None
        :type width: int, optional
        """
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
            self.font_size = self.font.size(text)

            if border_color is not None:
                self.border_rect = pygame.Rect(
                    self.position[0] - self.padding - self.border_size,
                    self.position[1] - self.padding - self.border_size,
                    self.font_size[0] + self.padding * 2 + self.border_size * 2,
                    self.font_size[1] + self.padding * 2 + self.border_size * 2
                )
            else:
                self.border_rect = None

            self.rect = pygame.Rect(
                self.position[0] - self.padding,
                self.position[1] - self.padding,
                self.font_size[0] + self.padding * 2,
                self.font_size[1] + self.padding * 2
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

    def get_rect(self) -> pygame.Rect:
        """Returns the rect containing both the position and width/height

        :return: tuple containing position x/y and width and height
        :rtype: pygame.Rect
        """
        return self.rect

    def create_wrapped_text_list(self, text: str, font: pygame.font.Font, width: int) -> Array:
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

    def render_text_lists(self, lines: Array) -> pygame.Surface:
        """creates a surface containing all the text wrapped

        :param lines: the text split into lines so it fits into the width passed in the init
        :type lines: Array
        :return: surface containing all the text and the background if any
        :rtype: pygame.Surface
        """
        rendered = [self.font.render(line, True, self.text_color).convert_alpha() for line in lines]

        line_height = self.font.get_linesize()
        width = max(line.get_width() for line in rendered)
        tops = [int(round(i * line_height)) for i in range(len(rendered))]
        height = tops[-1] + self.font.get_height()

        surface = pygame.Surface((width, height)).convert_alpha()
        if self.background_color != None:
            surface.fill(self.background_color)
        for y, line in zip(tops, rendered):
            surface.blit(line, (0, y))
        return surface

    def set_center_position(self, position: Tuple) -> None:
        """Set's the surface to the center of the passed position

        :param position: position dictionary with 4 values, first 2 being X/Y and next 2 being width/height
        :type position: Tuple
        """
        if self.border_rect is not None:
            self.border_rect.center = position
        self.rect.center = position
        self.text_rect.center = position

    def draw(self) -> None:
        """Draw method usually called in the screen to draw the textdisplay
        """
        super().draw()

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

    def handle_events(self, events: pygame.EventList) -> None:
        """Handles events passed to this container in the screen also passes the events to all the items inside the container to check in their own handle events function and handle accordingly

        :param events: Events to check
        :type events: pygame.EventList
        """
        super().handle_events(events)