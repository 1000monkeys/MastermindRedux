import pygame
from helpers.Button import Button
from helpers.Screen import Screen
from helpers.TextDisplay import TextDisplay


class MessageScreen(Screen):
    def __init__(self, display_manager, screen, localisation, assets, prompt_text, left_option_text, left_option_callback, right_option_text, right_option_callback) -> None:
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        
        self.prompt_text = prompt_text

        self.left_option_text = left_option_text
        self.left_option_callback = left_option_callback

        self.right_option_text = right_option_text
        self.right_option_callback = right_option_callback

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )

        self.texts = dict()
        self.texts["prompt_text"] = TextDisplay(
            screen=screen,
            text=self.prompt_text,
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=5,
            padding=25
        )
        self.texts["prompt_text"].set_center_position((1024/2, 786/2 - 200))

        self.buttons = dict()
        self.buttons["left_option"] = Button(
            screen,
            text=self.left_option_text,
            position=(256, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.left_option_callback
        )
        self.buttons["left_option"].set_center_position((256, 700))

        self.buttons["right_option"] = Button(
            screen,
            text=self.right_option_text,
            position=(768, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.right_option_callback
        )
        self.buttons["right_option"].set_center_position((768, 700))

    def draw(self):
        self.screen.blit(self.background_image, [0,0])

        for key in self.texts.keys():
            self.texts[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()

    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

