from calendar import c
from random import randrange
import pygame
from helpers.Button import Button
from helpers.Pin import Pin
from helpers.ResultPin import ResultPin

from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum
from helpers.TextDisplay import TextDisplay
from screens.MessageScreen import MessageScreen

class GameScreen(Screen):
    def __init__(self, display_manager, screen, localisation, assets, setting_screen_positions) -> None:
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.setting_screen_positions = setting_screen_positions

        self.rows, self.columns = (14, 4)

        self.background_image = pygame.transform.scale(
            self.assets.main_background_image,
            (1024, 786)
        )
        self.game_background_image = pygame.transform.scale(
            self.assets.game_background_image,
            (512, 786)
        )

        self.buttons = dict()
        self.buttons["exit"] = Button(
            screen,
            text=self.localisation.current_language["back"],
            position=(850, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )
        self.buttons["exit"].set_center_position((900, 700))

        self.buttons["guess"] = Button(
            screen,
            text="Guess!",
            position=(75, 700),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.end_turn
        )
        self.buttons["guess"].set_center_position((230, 675))

        self.texts = dict()
        self.texts["header"] = TextDisplay(
            screen,
            text="Mastermind!",
            position=(125, 50),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=48,
            border_size=5,
            padding=25
        )
        
        text = "Het spel gaat als volgt: De speler plaatst links 4 verschillende kleuren pionnetjes. Nadat je je gok doorstuurt komt in het rechter gedeelte een aantal zwarte en/of witte pionnetjes. Of geen." + \
        "Als je geen pionnen krijgt zijn alle kleuren en alle posities fout. Als je een zwarte pion krijgt betekent dat dat er een van de gekleurde pionnen op de juiste positie staat. Als je een witte pion krijgt " + \
        "is de kleur juist maar de positie onjuist. Let op! De posities van de zwarte en witte pionnen zijn niet gelinkt aan de posities van de gegokte kleuren."

        self.texts["explanation"] = TextDisplay(
            screen,
            text=text,
            position=(552, 200),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=24,
            border_size=5,
            padding=25,
            width=430
        )

        self.pin_array = []
        for j in range(self.rows):
            column = []
            for i in range(self.columns):
                column.append(Pin(screen, assets, (i, j)))
            self.pin_array.append(column)

        self.result_array = []
        for j in range(self.rows):
            column = []
            for i in range(self.columns):
                column.append(ResultPin(screen, assets, (i, j)))
            self.result_array.append(column)

        self.solution = []
        while len(self.solution) != 4:
            random = randrange(6)
            if random not in self.solution:
                self.solution.append(random)

        self.current_row = 0

        
    def exit_button(self):
        messageScreen = MessageScreen(
            self.display_manager,
            self.screen,
            self.localisation,
            self.assets,
            "Are you sure you want to quit?",
            "Yes",
            self.exit_screen,
            "No",
            self.stay_in_game
        )
        self.display_manager.set_message_screen(messageScreen)

    def restart_game(self):
        self.display_manager.screens[ScreenEnum.GAMESCREEN.value] = GameScreen(
            self.display_manager,
            self.screen,
            self.localisation,
            self.assets,
            self.setting_screen_positions
        )
        self.display_manager.set_message_screen(None)

    def exit_screen(self):
        self.display_manager.set_message_screen(None)
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def stay_in_game(self):
        self.display_manager.set_message_screen(None)

    def end_turn(self):
        changed = True
        for pin in self.pin_array[self.current_row]:
            if not pin.changed:
                changed = False
        
        guessed_code = [
            self.pin_array[self.current_row][0].color,
            self.pin_array[self.current_row][1].color,
            self.pin_array[self.current_row][2].color,
            self.pin_array[self.current_row][3].color
        ]

        print(self.solution)

        if changed or self.setting_screen_positions["empty_pin_pos"] == 1:
            black_pins = 0
            white_pins = 0
            checked_colors = list()
            for column in range(self.columns):
                if guessed_code[column] == self.solution[column] and guessed_code[column] not in checked_colors:
                    black_pins = black_pins + 1
                    checked_colors.append(guessed_code[column])
                    
            for column in range(self.columns):
                if guessed_code[column] in self.solution and guessed_code[column] not in checked_colors:
                    white_pins = white_pins + 1
                    checked_colors.append(guessed_code[column])

            result_position = 0
            for i in range(black_pins):
                self.result_array[self.current_row][result_position].set_black()
                result_position = result_position + 1
            for i in range(white_pins):
                self.result_array[self.current_row][result_position].set_white()
                result_position = result_position + 1
            self.current_row = self.current_row + 1

            if guessed_code == self.solution:
                message_screen = MessageScreen(
                    self.display_manager,
                    self.screen,
                    self.localisation,
                    self.assets,
                    "You won! Good job!!",
                    "Another game!",
                    self.restart_game,
                    "Quit to main menu!",
                    self.exit_button
                )

                self.display_manager.set_message_screen(message_screen)

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.screen.blit(self.game_background_image, [0, 0])

        for key in self.buttons.keys():
            self.buttons[key].draw()

        for key in self.texts.keys():
            self.texts[key].draw()

        for row in range(self.rows):
            for col in range(self.columns):
                self.pin_array[row][col].draw()

        for row in range(self.rows):
            for col in range(self.columns):
                self.result_array[row][col].draw()

    def handle_events(self, events):
        super().handle_events(events)

        for key in self.buttons.keys():
            self.buttons[key].handle_events(events)

        for row in range(self.rows):
            if row == self.current_row:
                for col in range(self.columns):
                    #print("row:" + str(row) + "col:" + str(col))
                    self.pin_array[row][col].handle_events(events)
