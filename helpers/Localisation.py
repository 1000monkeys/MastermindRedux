from helpers.SettingsEnum import SettingsEnum


class Localisation:
    def __init__(self, display_manager) -> None:
        self.display_manager = display_manager
        self.text_nl = dict()
        self.text_en = dict()

        self.neeJa = {0: "Nee", 1: "Ja"}
        self.noYes = {0: "No", 1: "Yes"}

        self.moeilijkheid = {0: "Makkelijk", 1: "Normaal", 2: "Moeilijk"}
        self.difficulty = {0: "Easy", 1: "Normal", 2: "Difficult"}

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
            str(SettingsEnum.AmountGameRounds.value.ONE.value),
            str(SettingsEnum.AmountGameRounds.value.TWO.value),
            str(SettingsEnum.AmountGameRounds.value.THREE.value),
            str(SettingsEnum.AmountGameRounds.value.FOUR.value),
            str(SettingsEnum.AmountGameRounds.value.FIVE.value),
            str(SettingsEnum.AmountGameRounds.value.TEN.value)
        ]
        self.text_en["amount_game_rounds_loop"] = self.text_nl["amount_game_rounds_loop"]

        self.text_nl["time_guess"] = "Tijd per gok:"
        self.text_en["time_guess"] = "Time for guess:"

        self.text_nl["time_guess_loop"] = [
            "Geen limiet",
            str(SettingsEnum.TimeGuess.value.FIFTEEN.value) + " seconden",
            str(SettingsEnum.TimeGuess.value.THIRTY.value) + " seconden",
            str(SettingsEnum.TimeGuess.value.SIXTY.value) + " seconden"
        ]
        self.text_en["time_guess_loop"] = [
            "No limit",
            str(SettingsEnum.TimeGuess.value.FIFTEEN.value) + " seconds",
            str(SettingsEnum.TimeGuess.value.THIRTY.value) + " seconds",
            str(SettingsEnum.TimeGuess.value.SIXTY.value) + " seconds"
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
        
        self.text_nl["empty_pins"] = "Lege pionnen:"
        self.text_en["empty_pins"] = "Empty pins:"

        self.text_nl["empty_pins_loop"] = [
            self.neeJa[SettingsEnum.EmptyPins.value.NO.value],
            self.neeJa[SettingsEnum.EmptyPins.value.YES.value] 
        ]
        self.text_en["empty_pins_loop"] = [
            self.noYes[SettingsEnum.EmptyPins.value.NO.value],
            self.noYes[SettingsEnum.EmptyPins.value.YES.value]
        ]

        self.text_nl["difficulty"] = "Verander huidige moeilijkheids instellingen naar:"
        self.text_en["difficulty"] = "Change current difficulty settings to:"

        self.text_nl["difficulty_loop"] = [
            self.moeilijkheid[SettingsEnum.Difficulty.value.EASY.value],
            self.moeilijkheid[SettingsEnum.Difficulty.value.NORMAL.value],
            self.moeilijkheid[SettingsEnum.Difficulty.value.DIFFICULT.value],
            
        ]
        self.text_en["difficulty_loop"] = [
            self.difficulty[SettingsEnum.Difficulty.value.EASY.value],
            self.difficulty[SettingsEnum.Difficulty.value.NORMAL.value],
            self.difficulty[SettingsEnum.Difficulty.value.DIFFICULT.value],
        ]

        self.text_nl["score_list_info"] = "Huidige instellingen hebben GEEN top score lijst"
        self.text_en["score_list_info"] = "Current settings have NO high score list"

        self.text_nl["save_and_exit"] = "Opslaan en terug"
        self.text_en["save_and_exit"] = "Save and go back"

        self.languages = {0: self.text_nl, 1: self.text_en}
        self.current_language_id = 0
        self.current_language = self.languages[self.current_language_id]

    def set_language(self, language_pos):
        self.current_language_id = language_pos
        self.current_language = self.languages[self.current_language_id]
