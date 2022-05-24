from operator import index, indexOf
from threading import local
from helpers.Assets import Assets
from helpers.Localisation import Localisation
from screens.MainMenu import MainMenu
from screens.Settings import Settings
from screens.HighScore import HighScore

class DisplayManager:
    def __init__(self, screen, localisation=None, setting_screen_positions=None, start_display_id=None) -> None:
        self.screen = screen
        if start_display_id is not None:
            self.screen_id = start_display_id
        else:
            self.screen_id = 0

        if localisation == None:
            self.localisation = Localisation(self)
        else:
            self.localisation = localisation

        self.assets = Assets()

        # Screen type to screen_id
        self.screens = list()
        self.screens.insert(0, MainMenu(self, screen, self.localisation, self.assets))
        if setting_screen_positions is not None:
            self.screens.insert(1, Settings(self, screen, self.localisation, self.assets, setting_screen_positions))
        else:
            self.screens.insert(1, Settings(self, screen, self.localisation, self.assets))
        self.screens.insert(2, HighScore(self, screen, self.localisation, self.assets))

    def get_current_screen_id(self):
        return self.screen_id

    def get_current_screen(self):
        return self.screens[self.screen_id]

    def change_screen(self, screen_id):
        self.screen_id = screen_id

