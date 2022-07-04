from helpers.Assets import Assets
from helpers.Localisation import Localisation
from helpers.Screen import Screen
from helpers.Enums.ScreenEnum import ScreenEnum
from screens.MainMenu import MainMenu
from screens.Settings import Settings

class DisplayManager:
    def __init__(self, screen: Screen, setting_screen_positions: dict, localisation: Localisation=None, start_display_id :int=None) -> None:
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
            ScreenEnum.HIGH_SCORE.value: None,
            ScreenEnum.GAMESCREEN.value: None
        }

    def set_message_screen(self, message_screen: Screen) -> None:
        self.message_screen = message_screen

    def get_current_screen_id(self) -> None:
        return self.screen_id
            
    def get_current_screen(self) -> Screen:
        return self.screens[self.screen_id]

    def change_screen(self, screen_id) -> None:
        self.screen_id = screen_id
