from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from helpers.DisplayManager import DisplayManager

from helpers.Enums.SettingsEnum import SettingsEnum

class Localisation:
    def __init__(self, display_manager: DisplayManager) -> None:
        self.display_manager = display_manager

        self.text_nl = dict()
        self.text_en = dict()

        self.neeJa = {0: "Nee", 1: "Ja"}
        self.noYes = {0: "No", 1: "Yes"}

        self.text_nl["no"] = self.neeJa[0]
        self.text_en["no"] = self.noYes[0]

        self.text_nl["yes"] = self.neeJa[1]
        self.text_en["yes"] = self.noYes[1]

        self.moeilijkheid = {0: "Makkelijk", 1: "Normaal", 2: "Moeilijk"}
        self.difficulty = {0: "Easy", 1: "Normal", 2: "Difficult"}

        self.time = {0: "None", 1: "15", 2: "30", 3:"60"}

        self.game_rounds = {0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "10"}

        self.amount_pins = {0: "4", 1: "5", 2: "6"}

        # Algemeen
        self.text_nl["back"] = "Terug"
        self.text_en["back"] = "Back"

        # MainMenu
        self.text_nl["welcome"] = "Welkom op Mastermind, Daag je brein uit!"
        self.text_en["welcome"] = "Welcome to Mastermind, Challenge your brain!"

        self.text_nl["play"] = "Spelen"
        self.text_en["play"] = "Play"

        self.text_nl["settings"] = "Instellingen"
        self.text_en["settings"] = "Settings"

        self.text_nl["highscore"] = "Top score"
        self.text_en["highscore"] = "High score"

        self.text_nl["exit"] = "Afsluiten"
        self.text_en["exit"] = "Exit"

        # HighScore
        self.text_nl["no_scores"] = "Er zijn nog geen top scores!"
        self.text_en["no_scores"] = "There are no high scores yet!"

        # Settings
        self.text_nl["option_menu"] = "Optie menu:"
        self.text_en["option_menu"] = "Option menu:"

        self.text_nl["description"] = "Klik op de optie(rechts) om door de opties te lussen!"
        self.text_en["description"] = "Click on the option(righthand side) to loop through the options!"

        self.text_nl["language"] = "Taal:"
        self.text_en["language"] = "Language:"

        self.text_nl["language_loop"] = [
            SettingsEnum.Language.value.NL.name,
            SettingsEnum.Language.value.EN.name
        ]
        self.text_en["language_loop"] = self.text_nl["language_loop"]

        self.text_nl["amount_game_rounds"] = "Aantal spel rondes:"
        self.text_en["amount_game_rounds"] = "Amount of game rounds:"

        self.text_nl["amount_game_rounds_loop"] = [
            self.game_rounds[SettingsEnum.AmountGameRounds.value.ONE.value],
            self.game_rounds[SettingsEnum.AmountGameRounds.value.TWO.value],
            self.game_rounds[SettingsEnum.AmountGameRounds.value.THREE.value],
            self.game_rounds[SettingsEnum.AmountGameRounds.value.FOUR.value],
            self.game_rounds[SettingsEnum.AmountGameRounds.value.FIVE.value],
            self.game_rounds[SettingsEnum.AmountGameRounds.value.TEN.value]
        ]
        self.text_en["amount_game_rounds_loop"] = self.text_nl["amount_game_rounds_loop"]

        self.text_nl["time_guess"] = "Tijd per gok:"
        self.text_en["time_guess"] = "Time for guess:"

        self.text_nl["time_guess_loop"] = [
            "Geen limiet",
            self.time[SettingsEnum.TimeGuess.value.FIFTEEN.value] + " seconden",
            self.time[SettingsEnum.TimeGuess.value.THIRTY.value] + " seconden",
            self.time[SettingsEnum.TimeGuess.value.SIXTY.value] + " seconden"
        ]
        self.text_en["time_guess_loop"] = [
            "No limit",
            self.time[SettingsEnum.TimeGuess.value.FIFTEEN.value] + " seconds",
            self.time[SettingsEnum.TimeGuess.value.THIRTY.value] + " seconds",
            self.time[SettingsEnum.TimeGuess.value.SIXTY.value] + " seconds"
        ]

        self.text_nl["repeating_colors"] = "Herhalende kleuren:"
        self.text_en["repeating_colors"] = "Repeating colors:"

        self.text_nl["repeating_colors_loop"] = [
            self.neeJa[SettingsEnum.RepeatingColors.value.NO.value],
            self.neeJa[SettingsEnum.RepeatingColors.value.YES.value]
        ]
        self.text_en["repeating_colors_loop"] = [
            self.noYes[SettingsEnum.RepeatingColors.value.NO.value],
            self.noYes[SettingsEnum.RepeatingColors.value.YES.value]
        ]
        
        self.text_nl["amount_pins"] = "Aantal pionnen:"
        self.text_en["amount_pins"] = "Amount of pins:"

        self.text_nl["amount_pins_loop"] = ["4", "5", "6"]
        self.text_en["amount_pins_loop"] = self.text_nl["amount_pins_loop"]

        self.text_nl["difficulty"] = "Verander huidige moeilijkheids instellingen naar:"
        self.text_en["difficulty"] = "Change current difficulty settings to:"

        self.text_nl["difficulty_loop"] = [
            self.moeilijkheid[SettingsEnum.Difficulty.value.EASY.value],
            self.moeilijkheid[SettingsEnum.Difficulty.value.NORMAL.value],
            self.moeilijkheid[SettingsEnum.Difficulty.value.HARD.value],
            
        ]
        self.text_en["difficulty_loop"] = [
            self.difficulty[SettingsEnum.Difficulty.value.EASY.value],
            self.difficulty[SettingsEnum.Difficulty.value.NORMAL.value],
            self.difficulty[SettingsEnum.Difficulty.value.HARD.value],
        ]

        self.text_nl["score_list_info"] = {
            -1: "Huidige instellingen hebben GEEN top score lijst",
            0: "Huidige instellingen hebben de MAKKELIJK top score lijst",
            1: "Huidige instellingen hebben de NORMAAL top score lijst",
            2: "Huidige instellingen hebben de MOEILIJK top score lijst"
        }
        self.text_en["score_list_info"] = {
            -1: "Current settings have NO high score list",
            0: "Current settings have the MAKKELIJK high score list",
            1: "Current settings have the NORMAAL high score list",
            2: "Current settings have the MOEILIJK high score list"
        }

        self.text_nl["save_and_exit"] = "Opslaan en terug"
        self.text_en["save_and_exit"] = "Save and go back"

        self.text_nl["game_description"] = "Het spel gaat als volgt: De speler plaatst links een aantal verschillende kleuren pionnetjes. Nadat je je gok doorstuurt komt in het rechter gedeelte een aantal zwarte en/of witte pionnetjes. Of geen." + \
        "Als je geen pionnen krijgt zijn alle kleuren en alle posities fout. Als je een zwarte pion krijgt betekent dat dat er een van de gekleurde pionnen op de juiste positie staat. Als je een witte pion krijgt " + \
        "is de kleur juist maar de positie onjuist. Let op! De posities van de zwarte en witte pionnen zijn niet gelinkt aan de posities van de gegokte kleuren." + \
        "Linker klik is vooruit in de kleuren en rechter klik is achteruit."
        self.text_en["game_description"] = "The game goes as follows: The player places a number colored pins. After you commit your guess you get a couple of black or white pins on the right part. Or none." + \
        "If you get no pins alle colors and pins are wrong. If you get a black pin that means one of the colored pins is in the right position. If you get a white pin " + \
        "the color is right but the position is wrong. Attention! The positions on the white and black pins are not linked to the colored pins." + \
        "Left click is forward through the colors and right click is backwards."

        self.text_nl["start_game"] = "Start game!"
        self.text_en["start_game"] = "Start game!"

        self.text_nl["guess"] = "Guess!"
        self.text_en["guess"] = self.text_nl["guess"]

        self.text_nl["header"] = "Mastermind!"
        self.text_en["header"] = self.text_nl["header"]

        self.text_nl["quit_text"] = "Weet je zeker dat je wilt aflsuiten?"
        self.text_en["quit_text"] = "Are you sure you want to quit?"

        self.text_nl["finished_game"] = "Je hebt het spel uitgespeeld! Goed gedaan!!"
        self.text_en["finished_game"] = "You finished the game! Good job!!"

        self.text_nl["another_game"] = "Nog een spel!"
        self.text_en["another_game"] = "Another game!"

        self.text_nl["quit_to_menu"] = "Terug naar hoofd menu!"
        self.text_en["quit_to_menu"] = "Quit to main menu!"

        self.text_nl["you_won"] = "Je hebt gewonnen! Goed gedaan!" 
        self.text_en["you_won"] = "You won! Good job!"

        self.text_nl["lost_next_round"] = "Je hebt verloren, Op naar de volgende ronde!"
        self.text_en["lost_next_round"] = "You lost, Onto the next round!"

        self.text_nl["next_round"] = "Volgende ronde!"
        self.text_en["next_round"] = "Next round!"

        self.text_nl["lost"] = "Je hebt verloren!"
        self.text_en["lost"] = "You lost!"

        self.text_nl["restart"] = "Spel herstarten!"
        self.text_en["restart"] = "Restart game!"

        self.text_nl["you_won"] = "Je hebt het gekraakt! Op naar de volgende ronde!"
        self.text_en["you_won"] = "You cracked it! Onto the next round!"\

        self.text_nl["name_info"] = "Min 1, Max 10, Alleen letters."
        self.text_nl["name_info_2"] = "Backspace om te verwijderen and dan typen om in te voeren!"
        self.text_en["name_info"] = "Min 1, Max 10, Alpha only."
        self.text_en["name_info_2"] = "Backspace to remove and then type to enter!"

        self.languages = {0: self.text_nl, 1: self.text_en}
        self.current_language_id = 0
        self.current_language = self.languages[self.current_language_id]

    def set_language(self, language_pos: int) -> None:
        self.current_language_id = language_pos
        self.current_language = self.languages[self.current_language_id]
