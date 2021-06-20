from screens.MainMenu import MainMenu

class DisplayManager:
    def __init__(self, pygame, screen) -> None:
        self.screen = screen
        self.main_menu = MainMenu(pygame, screen)

    def get_current_screen(self):
        return self.main_menu

    def set_current_screen(self, screen_id):
        self.screen_id = screen_id
    