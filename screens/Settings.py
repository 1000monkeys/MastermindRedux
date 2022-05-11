from ast import arg
from cgitb import text
import sys
from turtle import back
from typing import Text
from helpers.Button import Button
from helpers.Container import Container
from helpers.Screen import Screen
from helpers.TextDisplay import TextDisplay
from helpers.TextLoop import TextLoop

class Settings(Screen):
    def __init__(self, pygame, screen, display_manager) -> None:
        super().__init__()
        self.pygame = pygame
        self.screen = screen
        self.display_manager = display_manager

        self.background_image = pygame.transform.scale(
            pygame.image.load("assets/enigma.jpg"),
            (1024, 786)
        )

        self.texts = dict()
        self.text_loops = dict()

        self.texts["optie_menu"] = TextDisplay(
            screen,
            text="Optie menu:",
            position=(50, 50),
            text_color=(255, 255, 255),
            font_size=48
        )

        self.texts["taal"] = TextDisplay(
            screen,
            text="Taal:",
            position=(90, 125),
            font_size=36
        )
        self.text_loops["taal"] = TextLoop(
            screen,
            texts=["NL", "EN"],
            position=(800, 125),
            font_size=36
        )

        self.texts["aantal_spel_rondes"] = TextDisplay(
            screen,
            text="Aantal spel rondes:",
            position=(90, 175),
            font_size=36
        )       
        self.text_loops["aantal_spel_rondes"] = TextLoop(
            screen,
            texts=["1", "2", "4", "5", "10"],
            position=(800, 175),
            font_size=36
        )

        
        self.texts["tijd_per_gok"] = TextDisplay(
            screen,
            text="Tijd per gok:",
            position=(90, 225),
            font_size=36
        )
        self.text_loops["tijd_per_gok"] = TextLoop(
            screen,
            texts=["Geen limiet", "15 seconden", "30 seconden", "60 seconden"],
            position=(800, 225),
            font_size=36
        )

        self.texts["herhalende_kleuren"] = TextDisplay(
            screen,
            text="Herhalende kleuren:",
            position=(90, 275),
            font_size=36
        )
        self.text_loops["herhalende_kleuren"] = TextLoop(
            screen,
            texts=["Ja", "Nee"],
            position=(800, 275),
            font_size=36
        )


        self.texts["lege_pionnen"] = TextDisplay(
            screen,
            text="Lege pionnen:",
            position=(90, 325),
            font_size=36
        )
        self.text_loops["lege_pionnen"] = TextLoop(
            screen,
            texts=["Ja", "Nee"],
            position=(800, 325),
            font_size=36
        )


        self.texts["moeilijkheid"] = TextDisplay(
            screen,
            text="Verander huidige moeilijkheids instellingen naar:",
            position=(65, 375),
            font_size=36
        )
        self.text_loops["moeilijkheid"] = TextLoop(
            screen,
            texts=["Normaal", "Moeilijk"],
            position=(800, 375),
            font_size=36
        )
        
        self.texts["score_list_info"] = TextDisplay(
            screen,
            text="Huidige instellingen hebben GEEN top score lijst",
            position=(180, 450),
            font_size=36
        )

        self.merged_items = self.merge_dict(self.texts, self.text_loops)
        self.container = Container(
            screen,
            self.merged_items,
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            border_size=10,
            padding=10
        )

        self.buttons = dict()
        self.buttons["back"] = Button(
            screen,
            text="Back",
            position=(925, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            callback_function=self.back
        )

    def back(self):
        self.display_manager.change_screen(0)

    def merge_dict(self, *args):
        result = dict()
        dict_count = 0
        for dictionary in args:
            for key in dictionary.keys():
                result[str(dict_count) + "-" + str(key)] = dictionary[key]
            dict_count = dict_count + 1
        return result

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.container.draw()

        """
        for key in self.texts.keys():
            self.texts[key].draw()
        """

        for key in self.text_loops.keys():
            self.text_loops[key].draw()

        for key in self.buttons.keys():
            self.buttons[key].draw()
        
    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

        for key in self.text_loops.keys():
            self.text_loops[key].handle_events(events)
        # for event in events:
