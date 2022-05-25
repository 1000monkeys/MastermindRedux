from threading import local
from helpers.Button import Button
from helpers.Container import Container
from helpers.StaticFunctions import StaticFunctions
from helpers.TextDisplay import TextDisplay


class MessageBox():
    def __init__(self, screen, prompt_text, left_option_text, right_option_text) -> None:
        self.screen = screen
        self.prompt_text = prompt_text
        self.left_option_text = left_option_text
        self.right_option_text = right_option_text

        self.texts = dict()
        self.texts["prompt_text"] = TextDisplay(
            screen,
            text=self.prompt_text,
            position=(150, 200),
            text_color=(255, 255, 255),
            font_size=48
        )
        
        self.buttons = dict()
        self.buttons["left_option"] = Button(
            screen,
            text=self.left_option_text,
            position=(200, 300),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5
        )
        self.buttons["right_option"] = Button(
            screen,
            text=self.right_option_text,
            position=(450, 300),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5
        )

        self.merged_items = StaticFunctions.merge_dict(self.texts, self.buttons)
        self.container = Container(
            screen,
            self.merged_items,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=10
        )

    def draw(self):
        self.container.draw()

    def handle_events(self, events):
        pass
