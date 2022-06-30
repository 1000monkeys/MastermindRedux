import collections
import json
from operator import itemgetter
from os import path
from random import randrange
import time
from tkinter.font import NORMAL
import pygame
from helpers.Button import Button
from helpers.DifficultyEnum import DifficultyEnum
from helpers.Pin import Pin
from helpers.ResultPin import ResultPin

from helpers.Screen import Screen
from helpers.ScreenEnum import ScreenEnum
from helpers.SettingsEnum import SettingsEnum
from helpers.TextDisplay import TextDisplay
from screens.MessageScreen import MessageScreen

class GameScreen(Screen):
    def __init__(self, display_manager, screen, localisation, assets, setting_screen_positions) -> None:
        self.display_manager = display_manager
        self.screen = screen
        self.localisation = localisation
        self.assets = assets
        self.setting_screen_positions = setting_screen_positions

        self.amount_rounds = int(self.localisation.game_rounds[self.setting_screen_positions["game_rounds_pos"]])
        self.amount_pins = int(self.localisation.amount_pins[self.setting_screen_positions["amount_pins_pos"]])
        self.assets.arrows = pygame.transform.scale(self.assets.arrows, (68 + (32 * (6 - self.amount_pins)), 60))
        self.time = self.localisation.time[self.setting_screen_positions["time_guess_pos"]]
        if self.time == 'None':
            self.time = 0
        else:
            self.time = int(self.time)
    
        self.rows, self.columns = (14, self.amount_pins)

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
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.exit_button
        )
        self.buttons["exit"].set_center_position((900, 700))

        self.buttons["guess_start"] = Button(
            screen,
            text=self.localisation.current_language["start_game"],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.start_game  
        )
        if self.time != 0:
            self.buttons["guess_start"].set_center_position((384, 700))
        else:
            self.buttons["guess_start"].set_center_position((256, 700))


        self.texts = dict()
        self.texts["header"] = TextDisplay(
            screen,
            text=self.localisation.current_language["header"],
            position=(125, 50),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=48,
            border_size=5,
            padding=25
        )
        self.texts["explanation"] = TextDisplay(
            screen,
            text=self.localisation.current_language["game_description"],
            position=(552, 200),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=24,
            border_size=5,
            padding=25,
            width=430
        )
        if self.time != 0:
            self.texts["timer"] = TextDisplay(
                screen,
                text="0",
                position=(0, 0),
                text_color=(255, 255, 255),
                background_color=(55, 42, 34),
                border_color=(255, 255, 255),
                font_size=32,
                border_size=5,
                padding=5,
                width=50
            )
            self.texts["timer"].set_center_position((128, 700))
        
        self.difficulty = self.display_manager.screens[ScreenEnum.SETTINGS.value].get_difficulty()
        if self.difficulty != 0:
            self.texts["score"] = TextDisplay(
                self.screen,
                text="Score: " + str(0),
                position=(0, 0),
                text_color=(255, 255, 255),
                background_color=(55, 42, 34),
                border_color=(255, 255, 255),
                font_size=32,
                border_size=5,
                padding=5
            )
            self.texts["score"].set_center_position((640, 700))

        self.create_pins()
        self.create_solution()

        self.current_row = 0
        self.round = 0
        self.start_time = 0
        self.score_start_time = 0
        self.current_time = 0
        self.game_started = False
        self.score = dict()
        self.amount_rounds=1

    def create_pins(self):
        self.pin_array = []
        for j in range(self.rows):
            column = []
            for i in range(self.columns):
                column.append(Pin(self.screen, self.assets, (i, j), max_pin=self.amount_pins + 2))
            self.pin_array.append(column)

        self.result_array = []
        for j in range(self.rows):
            column = []
            for i in range(self.columns):
                column.append(ResultPin(self.screen, self.assets, (i, j)))
            self.result_array.append(column)


    def create_solution(self):
        self.solution = []
        while len(self.solution) != self.amount_pins:
            random = randrange(self.amount_pins + 2)
            if random not in self.solution:
                self.solution.append(random)
        print("Solution:" + str(self.solution))

    def start_game(self):
        self.buttons["guess_start"] = Button(
            self.screen,
            text=self.localisation.current_language["guess"],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.end_turn
        )
        if self.time != 0:
            self.buttons["guess_start"].set_center_position((384, 700))
        else:
            self.buttons["guess_start"].set_center_position((256, 700))
        self.start_time = int(time.time())
        self.score_start_time = int(time.time())
        self.game_started = True
        self.round = 1
        self.difficulty = self.display_manager.screens[ScreenEnum.SETTINGS.value].get_difficulty()
        self.update_timer_text()

    def exit_button(self):
        messageScreen = MessageScreen(
            self.display_manager,
            self.screen,
            self.localisation,
            self.assets,
            self.localisation.current_language["quit_text"],
            self.localisation.current_language["yes"],
            self.exit_screen,
            self.localisation.current_language["no"],
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
        self.buttons["guess_start"] = Button(
            self.screen,
            text=self.localisation.current_language["start_game"],
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            font_size=36,
            border_size=5,
            padding=5,
            callback_function=self.end_turn
        )
        if self.time != 0:
            self.buttons["guess_start"].set_center_position((384, 700))
        else:
            self.buttons["guess_start"].set_center_position((256, 700))
        self.start_time = int(time.time())
        self.score_start_time = int(time.time())
        self.game_started = False
        self.display_manager.set_message_screen(None)

    def next_round(self):
        self.create_solution()
        self.create_pins()
        self.game_started = True
        self.start_time = int(time.time())
        self.round = self.round + 1
        self.current_row = 0
        self.display_manager.set_message_screen(None)

    def exit_screen(self):
        self.display_manager.set_message_screen(None)
        self.display_manager.change_screen(ScreenEnum.MAIN_MENU.value)

    def stay_in_game(self):
        self.display_manager.set_message_screen(None)

    def calculate_score(self):
        temp_score = (14 - self.current_row) * 100
        
        if self.difficulty == DifficultyEnum.NORMAL.value:
            temp_score = temp_score + ((14 - self.current_row) * 50)
        if self.difficulty == DifficultyEnum.DIFFICULT.value:
            temp_score = temp_score + ((14 - self.current_row) * 50)
        
        if self.time != 0:
            temp_score = round((temp_score / self.time) * ((self.time * 14 + 14) - (self.current_time - self.score_start_time)))

        self.score[self.round] = temp_score

    def end_turn(self):
        guessed_code = list()
        amount_pins = int(self.localisation.amount_pins[self.setting_screen_positions["amount_pins_pos"]])
        for index in range(amount_pins):
            guessed_code.append(self.pin_array[self.current_row][index].color_pos)

        print("Guessed code:" + str(guessed_code))

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

        if guessed_code == self.solution and self.amount_rounds == self.round:
            message_screen = MessageScreen(
                self.display_manager,
                self.screen,
                self.localisation,
                self.assets,
                self.localisation.current_language["you_won"] + " Score is " + str(self.score[self.round]),
                self.localisation.current_language["another_game"],
                self.restart_game,
                self.localisation.current_language["quit_to_menu"],
                self.exit_button
            )
            self.display_manager.set_message_screen(message_screen)
            self.game_started = False
            self.update_score()
        elif self.current_row == 13 and guessed_code != self.solution:
            if self.round != self.amount_rounds:
                message_screen = MessageScreen(
                    self.display_manager,
                    self.screen,
                    self.localisation,
                    self.assets,
                    self.localisation.current_language["lost_next_round"],
                    self.localisation.current_language["next_round"],
                    self.next_round,
                    self.localisation.current_language["quit_to_menu"],
                    self.exit_button
                )
                self.display_manager.set_message_screen(message_screen)
                self.game_started = False
            else:
                message_screen = MessageScreen(
                    self.display_manager,
                    self.screen,
                    self.localisation,
                    self.assets,
                    self.localisation.current_language["lost"],
                    self.localisation.current_language["restart"],
                    self.restart_game,
                    self.localisation.current_language["quit_to_menu"],
                    self.exit_button
                )
                self.display_manager.set_message_screen(message_screen)
                self.game_started = False
        elif guessed_code == self.solution and self.amount_rounds != self.round:
            message_screen = MessageScreen(
                self.display_manager,
                self.screen,
                self.localisation,
                self.assets,
                self.localisation.current_language["you_won"] + " Score is " + str(self.score[self.round]),
                self.localisation.current_language["next_round"],
                self.next_round,
                self.localisation.current_language["quit_to_menu"],
                self.exit_button
            )
            self.display_manager.set_message_screen(message_screen)
            self.game_started = False
        else:
            self.calculate_score()
            self.current_row = self.current_row + 1
            self.start_time = int(time.time())

    def update_score(self):
        scores = self.open_score()

        temp_score = 0
        for score in self.score:
            temp_score = temp_score + self.score[score]

        scores[self.setting_screen_positions["name"]] = temp_score
        with open(str(self.difficulty) + 'high_scores.json', 'w') as f:
            f.write(json.dumps(scores))

    def open_score(self):
        if path.exists(str(self.difficulty) + "high_scores.json"):
            with open('high_scores.json') as f:
                scores = json.load(f)
                scores = collections.OrderedDict(scores)
                return scores
        else:
            return collections.OrderedDict()

    def update_timer_text(self):
        self.current_time = int(time.time())
        if self.time != 0 and self.start_time + self.time < self.current_time:
            self.end_turn()
            self.start_time = int(time.time())

        self.texts["timer"] = TextDisplay(
            self.screen,
            text=str(self.start_time + self.time - self.current_time),
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=32,
            border_size=5,
            padding=5
        )
        self.texts["timer"].set_center_position((128, 700))

    def update_score_text(self): 
        self.calculate_score()

        temp_score = 0
        for score in self.score:
            temp_score = temp_score + self.score[score]

        self.texts["score"] = TextDisplay(
            self.screen,
            text="Score: " + str(temp_score),
            position=(0, 0),
            text_color=(255, 255, 255),
            background_color=(55, 42, 34),
            border_color=(255, 255, 255),
            font_size=32,
            border_size=5,
            padding=5
        )
        self.texts["score"].set_center_position((640, 700))

    def draw(self):
        self.screen.blit(self.background_image, [0,0])
        self.screen.blit(self.game_background_image, [0, 0])

        if self.game_started:
            self.update_timer_text()
            self.update_score_text()

        self.screen.blit(self.assets.arrows, [220 - (32 * (6 - self.amount_pins)), 32 * self.current_row + 132])

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

        if self.game_started:
            for row in range(self.rows):
                if row == self.current_row:
                    for col in range(self.columns):
                        self.pin_array[row][col].handle_events(events)
