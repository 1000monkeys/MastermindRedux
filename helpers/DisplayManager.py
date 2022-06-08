from email.message import Message
from helpers.Assets import Assets
from helpers.Localisation import Localisation
from helpers.ScreenEnum import ScreenEnum
from screens.GameScreen import GameScreen
from screens.MainMenu import MainMenu
from screens.MessageScreen import MessageScreen
from screens.Settings import Settings
from screens.HighScore import HighScore

class DisplayManager:
    def __init__(self, screen, setting_screen_positions, localisation=None, start_display_id=None) -> None:
        self.screen = screen
        if start_display_id is not None:
            self.screen_id = start_display_id
        else:
            self.screen_id = 0

        if localisation == None:
            self.localisation = Localisation(self)
            self.localisation.set_language(setting_screen_positions["language_pos"])
        else:
            self.localisation = localisation

        self.assets = Assets()

        self.message_screen = None

        # Screen type to screen_id
        self.screens = {
            ScreenEnum.MAIN_MENU.value: MainMenu(self, screen, self.localisation, self.assets),
            ScreenEnum.SETTINGS.value: Settings(self, screen, self.localisation, self.assets, setting_screen_positions),
            ScreenEnum.HIGH_SCORE.value: HighScore(self, screen, self.localisation, self.assets),
            ScreenEnum.GAMESCREEN.value: GameScreen(self, screen, self.localisation, self.assets, setting_screen_positions)
        }

    def set_message_screen(self, message_screen):
        self.message_screen = message_screen

    def get_current_screen_id(self):
        if self.message_screen is None:
            return self.screen_id
        else:
            return ScreenEnum.MESSAGESCREEN.value
            
    def get_current_screen(self):
        if self.message_screen is None:
            return self.screens[self.screen_id]
        else:
            return self.message_screen

    def change_screen(self, screen_id):
        self.screen_id = screen_id
